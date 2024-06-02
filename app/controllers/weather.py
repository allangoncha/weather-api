from app.services.weather import WeatherService

class WeatherController:
    async def get(req, weather_service: WeatherService):
        return await weather_service.process_request(req)