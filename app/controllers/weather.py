from app.services.weather import WeatherService

class WeatherController:
    async def get(req, weatherService: WeatherService):
        return await weatherService.process_request(req)