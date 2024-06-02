from dotenv import load_dotenv
from pymongo import MongoClient
import os, requests, json

load_dotenv()
URL = os.getenv("url")
API_KEY = os.getenv("api_key")
MONGODB_HOST = os.getenv("mongodb_host")
MONGODB_PORT = os.getenv("mongodb_port")
MONGODB_USER = os.getenv("mongodb_user")
MONGODB_PASS = os.getenv("mongodb_pass")

class WeatherService:
    def __init__(self):

        try:
            #Init MongoClient
            self.client = MongoClient()
            self.client = MongoClient(f"mongodb://{MONGODB_USER}:{MONGODB_PASS}@{MONGODB_HOST}:{MONGODB_PORT}/")
            
        except Exception as e:
            raise e

    async def process_request(self, request):

        db = self.client['weather']
        collection = db['weather_datas']

        params = {
            'lat': request.lat,
            'lon': request.lon,
            'appid': API_KEY,
            'cnt': request.cnt,
            'units': request.units,
            'lang': 'pt_br'
        }

        response = requests.request("GET", URL, params=params)

        if response.status_code == 200:
            res = json.loads(response.text)
            inserted_id = collection.insert_one(res).inserted_id
            res['_id'] = str(inserted_id)
            return res
        
        else:
            return {"Error": {
                "msg": "Erro de retorno openweatherapi",
                "status": response.status_code,
            }}
        