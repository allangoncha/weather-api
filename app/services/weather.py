from dotenv import load_dotenv
import pymongo, os, requests, json

load_dotenv()
URL = os.getenv("url")
API_KEY = os.getenv("api_key")

class WeatherService:
    def __init__(self):
        pass

    async def process_request(self, request):
        params = {
            'lat': request.lat,
            'lon': request.lon,
            'appid': API_KEY,
            'cnt': request.cnt,
            'units': request.units,
            'lang': 'pt_br'
        }

        response = requests.request("GET", URL, params=params)

        return json.loads(response.text)