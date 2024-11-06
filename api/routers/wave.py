from fastapi import APIRouter, HTTPException
from services.wave_service import fetch_wave_data
from services.wave_chat_service import fetch_wave_and_chat

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

@router.get("/wave/{point}/chat")
async def get_wave_and_chat(point: str):
    try:
        response = await fetch_wave_and_chat(point)
        return response
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
