from typing import Optional
from pydantic import BaseModel, conint

class WeatherReq(BaseModel):
    lat: float
    lon: float
    cnt: int
    units: Optional[str] = 'metric'

class WeatherReqByCity(BaseModel):
    city: str

class WeatherReqHistory(BaseModel):
    limit: int