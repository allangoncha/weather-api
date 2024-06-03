from dotenv import load_dotenv
from pymongo import MongoClient
import os, requests, json, logging, sys, mongomock

load_dotenv()
URL = os.getenv("url")
API_KEY = os.getenv("api_key")
MONGODB_HOST = os.getenv("mongodb_host")
MONGODB_PORT = os.getenv("mongodb_port")
MONGODB_USER = os.getenv("mongodb_user")
MONGODB_PASS = os.getenv("mongodb_pass")

logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger(__name__)

class WeatherService:
    def __init__(self):

        try:
            if os.getenv("SAVE_TO_MONGO") == "True":
                self.client = mongomock.MongoClient()
            else:
                #Init MongoClient
                self.client = MongoClient()
                self.client = MongoClient(f"mongodb://{MONGODB_USER}:{MONGODB_PASS}@{MONGODB_HOST}:{MONGODB_PORT}/")
            
        except Exception as e:
            logger.error("Erro ao inicializar o cliente MongoDB", exc_info=True)

    async def process_request(self, request):
        logger.info("Realizando requisição para obter dados do clima.")
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

            try:
                logger.info("Requisição bem-sucedida. Inserindo dados no banco de dados.")
                res = json.loads(response.text)
                inserted_id = collection.insert_one(res).inserted_id
                res['_id'] = str(inserted_id)
                return res
            
            except Exception as e:
                raise e
        
        else:
            logger.error("Erro de retorno da openweatherapi. Status code: %s", response.status_code)
            return {"Error": {
                "msg": "Erro de retorno openweatherapi",
                "status": response.status_code,
            }}
    
    def close_connection(self):
        try:
            self.client.close()
            logger.info("Conexão com o MongoDB fechada com sucesso")
        except Exception as e:
            logger.error("Erro ao fechar a conexão com o MongoDB", exc_info=True)