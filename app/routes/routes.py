from fastapi import Depends
from app import app
from app.schemas.weather import WeatherReq
from app.controllers.weather import WeatherController
from app.services.weather import WeatherService

def get_weather_service():
    return WeatherService()

@app.get("/weather")
async def weatherReq(req: WeatherReq, weather_service: WeatherService = Depends(get_weather_service)):
    return await WeatherController.get(req, weather_service)
