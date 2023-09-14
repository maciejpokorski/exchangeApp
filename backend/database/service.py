from sqlmodel import Session, desc, update, select
from database.models.currency import Currency
from database.models.exchange_rate import ExchangeRate

def get_currencies(session: Session):
    """
    Get a list of currencies ordered by enabled status in descending order.

    Args:
        session (Session): The SQLModel session.

    Returns:
        List[Currency]: A list of Currency objects.
    """
    return session.exec(select(Currency).order_by(desc(Currency.enabled))).all()

def get_enabled_currencies(session: Session):
    """
    Get a list of enabled currencies.

    Args:
        session (Session): The SQLModel session.

    Returns:
        List[Currency]: A list of enabled Currency objects.
    """
    return session.exec(select(Currency).where(Currency.enabled == True)).all()

def update_currency(session: Session, currency_id: int, enabled: bool):
    """
    Update the enabled status of a currency.

    Args:
        session (Session): The SQLModel session.
        currency_id (int): The ID of the currency to update.
        enabled (bool): The new enabled status (True or False).
    """
    currency = session.get(Currency, currency_id)
    currency.enabled = enabled
    session.add(currency)
    session.commit()
    session.refresh(currency)
    return currency

def get_exchange_rates(session: Session):
    """
    Get a list of exchange rates ordered by date in descending order.

    Args:
        session (Session): The SQLModel session.

    Returns:
        List[ExchangeRate]: A list of ExchangeRate objects.
    """
    return session.exec(select(ExchangeRate).order_by(desc(ExchangeRate.date))).all()

def save_exchange_rate(session: Session, exchange_rate: ExchangeRate):
    """
    Save an ExchangeRate object to the database.

    Args:
        session (Session): The SQLModel session.
        exchange_rate (ExchangeRate): The ExchangeRate object to be saved.

    Returns:
        ExchangeRate: The saved ExchangeRate object.
    """
    session.add(exchange_rate)
    session.commit()
    session.refresh(exchange_rate)
    return exchange_rate
