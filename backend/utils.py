from constants import API_KEY
import httpx

def build_openexchangerates_url_and_params(date: str, api_key = API_KEY):
    base_url = "https://openexchangerates.org/api/historical/"
    request_url = f"{base_url}{date}.json"
    request_params = {"app_id": api_key}
    return request_url, request_params

async def fetch_remote_data(date: str, http_client=None):
    """
    Fetch remote exchange rate data for a given date.

    Args:
        date (str): The date in YYYY-MM-DD format.
        http_client (httpx.AsyncClient, optional): An HTTP client (for testing purposes).

    Returns:
        dict: A dictionary containing exchange rates.
    
    Raises:
        Exception: If the API request fails or returns an error.
    """
    request_url, request_params = build_openexchangerates_url_and_params(date)

    async with (http_client or httpx.AsyncClient()) as client:
        response = await perform_http_request(client, request_url, request_params)

        # Check if the response is valid
        if response.status_code == 200:
            return response.json().get("rates")
        else:
            raise Exception(response.text)

async def perform_http_request(client, url, params):
    """
    Perform an HTTP GET request and return the response.

    Args:
        client (httpx.AsyncClient): An HTTP client instance.
        url (str): The URL for the GET request.
        params (dict): Request parameters.

    Returns:
        httpx.Response: The HTTP response.
    """
    return await client.get(url, params=params)