import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool
from main import app, get_session, get_rates_for_given_currencies
from utils import fetch_remote_data
from unittest.mock import patch
from database.models.currency import Currency
from datetime import date, timedelta

@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


@pytest.fixture(name="client")
def client_fixture(session: Session):
    def get_session_override():
        return session

    def fetch_remote_data_override():
        return {"rates": {"EUR": 1.0, "USD": 1.2}}

    app.dependency_overrides[get_session] = get_session_override
    app.dependency_overrides[fetch_remote_data] = fetch_remote_data_override
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()


@pytest.mark.asyncio
async def test_fetch_data_success(client: TestClient):
    with patch('main.fetch_remote_data') as mock_fetch_remote_data:
        mock_fetch_remote_data.return_value = {
            "EUR": 0.85,
            "USD": 1.0,
            "JPY": 110.0,
            "GBP": 0.73,
        }

        with patch('main.get_enabled_currencies') as mock_get_enabled_currencies:
            enabled_currency_data = [
                {"code": "EUR", "enabled": True},
            ]
            enabled_currencies = [Currency(**data) for data in enabled_currency_data]
            mock_get_enabled_currencies.return_value = enabled_currencies

            test_date = "2023-09-14"
            result = client.get(f"/fetch_remote_data/{test_date}").json()

            assert "error" not in result
            assert result == {"EUR": 0.85}

@pytest.mark.asyncio
async def test_fetch_data_invalid_date(client: TestClient):
    test_date = "20223-09-14"
    result = client.get(f"/fetch_remote_data/{test_date}").json()

    assert "error" in result

    test_date = (date.today() + timedelta(days=1)).strftime("%Y-%m-%d")
    result = client.get(f"/fetch_remote_data/{test_date}").json()

    assert "error" in result

@pytest.mark.asyncio
async def test_fetch_data_error_from_remote(client: TestClient):
    # Mock the fetch_remote_data function (replace with your actual function)
    with patch('main.fetch_remote_data') as mock_fetch_remote_data:
        # Mock the return value of fetch_remote_data
        mock_fetch_remote_data.return_value = {
            "Error"
        }

        test_date = "2023-09-14"
        result = client.get(f"/fetch_remote_data/{test_date}").json()

        # Assertions
        assert "error" not in result  # Check for no error in the result

@pytest.mark.parametrize(
    "rates, currencies, expected_result",
    [
        ({'USD': 1.0, 'EUR': 0.85, 'GBP': 0.73}, ['USD', 'EUR'], {'USD': 1.0, 'EUR': 0.85}),
        ({'USD': 1.0, 'EUR': 0.85, 'GBP': 0.73}, ['USD', 'GBP'], {'USD': 1.0, 'GBP': 0.73}),
        ({'USD': 1.0, 'EUR': 0.85, 'GBP': 0.73}, ['JPY', 'CAD'], {}),
        ({}, ['USD', 'EUR'], {}),
        ({'USD': 1.0, 'EUR': 0.85, 'GBP': 0.73}, [], {}),
    ]
)
def test_get_rates_for_given_currencies(rates, currencies, expected_result):
    result = get_rates_for_given_currencies(rates, currencies)
    assert result == expected_result

def test_read_currencies(session: Session, client: TestClient):
    response = client.get("/get_currencies")
    data = response.json()

    assert response.status_code == 200
    assert data[0]["code"] == "EUR"