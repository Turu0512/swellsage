from fastapi import APIRouter, HTTPException
from services.wave_service import fetch_wave_data

router = APIRouter()

@router.get("/wave/{point}")
async def get_wave_data(point: str):
    try:
        wave_data = await fetch_wave_data(point)
        return {"wave_data": wave_data}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
