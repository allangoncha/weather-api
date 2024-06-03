from fastapi import Depends, Query
from app import app
from app.schemas.weather import WeatherReq, WeatherReqByCity, WeatherReqHistory
from app.controllers.weather import WeatherController
from app.services.weather import WeatherService

def getWeatherService():
    return WeatherService()

@app.get("/weather")
async def weatherReq(
    lat: float = Query(..., description="Latitude"),
    lon: float = Query(..., description="Longitude"),
    cnt: int = Query(5, ge=1, le=40, description="Número de dia para previsão (1-40)"),
    units: str = Query('metric', description="Unidade de medição (standard/metric/imperial)"), weatherService: WeatherService = Depends(getWeatherService)):
    req = WeatherReq(lat=lat, lon=lon, cnt=cnt, units=units)
    return await WeatherController.get(req, weatherService)

@app.get("/weather-by-city")
async def weatherReqCity(
    city: str = Query(..., description="city"),
    weatherService: WeatherService = Depends(getWeatherService)):
    req = WeatherReqByCity(city=city)
    return await WeatherController.getByCity(req, weatherService)

@app.get("/history")
async def weatherReqHistory(
    limit: int = Query(1, ge=1, le=100, description= "Limite de registros retornador"),
    weatherService: WeatherService = Depends(getWeatherService)):
    req = WeatherReqHistory(limit=limit)
    return await WeatherController.getHistory(req, weatherService)