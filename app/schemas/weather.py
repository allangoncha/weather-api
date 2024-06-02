from typing import Optional
from pydantic import BaseModel, conint

class WeatherReq(BaseModel):
    lat: float
    lon: float
    cnt: conint(ge=1, le=40) = 5
    units: Optional[str] = 'metric'
