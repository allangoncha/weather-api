import pytest, os
from httpx import AsyncClient
from app import app

@pytest.mark.asyncio
async def test_weather_endpoint():
    os.environ["SAVE_TO_MONGO"] = "True"
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/weather", params={"lat": 40.7128, "lon": -74.0060, "cnt": 5, "units": "metric"})
    assert response.status_code == 200
    data = response.json()
    assert "list" in data

@pytest.mark.asyncio
async def test_weather_endpoint_invalid_cnt():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/weather", params={"lat": 40.7128, "lon": -74.0060, "cnt": 50, "units": "metric"})
    assert response.status_code == 422

@pytest.mark.asyncio
async def test_weather_endpoint_missing_params():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/weather", params={"lat": 40.7128, "lon": -74.0060})
    assert response.status_code == 200
    data = response.json()
    assert "list" in data
