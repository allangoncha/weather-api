from app import app
from app.schemas.weather import WeatherReq
from app.controllers.weather import WeatherController

@app.get("/weather")
async def weatherReq(req: WeatherReq):
    return await WeatherController.get(req)
