from app.services.weather import WeatherService

ws = WeatherService()

class WeatherController:
    async def get(req):
        return await ws.process_request(req)