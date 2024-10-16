import os
import httpx
from fastapi import HTTPException
from typing import Dict, Any

async def fetch_wave_data(point: str) -> Dict[str, Any]:
    coords = os.getenv(f"REACT_APP_{point.upper()}_COORDS", "000,000")
    latitude, longitude = coords.split(',')

    base_url = "https://marine-api.open-meteo.com/v1/marine"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "swell_wave_height",
        "hourly": ["wave_height", "wave_direction", "wind_wave_height", "wind_wave_direction", "swell_wave_height", "swell_wave_direction"],
        "timezone": "Asia/Tokyo"
    }

    if longitude == '000':
        raise HTTPException(status_code=400, detail="Invalid longitude")

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(base_url, params=params)
            response.raise_for_status()
            wave_data = response.json()["hourly"]
            return wave_data
        except httpx.HTTPStatusError as e:
            print(f"HTTP error occurred: {e}")
            raise HTTPException(status_code=e.response.status_code, detail=str(e))
        except Exception as e:
            print(f"An error occurred: {e}")
            raise HTTPException(status_code=500, detail="Internal server error")
