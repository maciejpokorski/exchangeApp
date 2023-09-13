from constants import API_KEY
import httpx

def build_openexchangerates_url_and_params(date: str):
    base_url = "https://openexchangerates.org/api/historical/"
    request_url = f"{base_url}{date}.json"
    request_params = {"app_id": API_KEY}
    return request_url, request_params

async def fetch_remote_data(date: str):
    request_url, request_params = build_openexchangerates_url_and_params(date)

    async with httpx.AsyncClient() as client:
        response = await client.get(request_url, params=request_params)

        # check if response is valid
        if response.status_code == 200:
            return response.json().get("rates")
        else:
            raise Exception(response.text)