from app.services.weather import WeatherService

class WeatherController:
    async def get(req, weatherService: WeatherService):
        try:
            result = await weatherService.process_request(req)
            return result
        finally:
            weatherService.close_connection()
    
    async def getByCity(req, weatherService: WeatherService):
        try:
            result = await weatherService.process_request_city(req)
            return result
        finally:
            weatherService.close_connection()
    
    async def getHistory(req, weatherService: WeatherService):
        try:
            result = await weatherService.process_request_history(req)
            return result
        finally:
            weatherService.close_connection()