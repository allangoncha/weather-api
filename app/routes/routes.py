from fastapi import Depends
from app import app
from app.schemas.weather import WeatherReq
from app.controllers.weather import WeatherController
from app.services.weather import WeatherService

def getWeatherService():
    return WeatherService()

@app.get("/weather")
async def weatherReq(req: WeatherReq, weatherService: WeatherService = Depends(getWeatherService)):
    return await WeatherController.get(req, weatherService)
