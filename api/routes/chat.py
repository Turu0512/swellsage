from fastapi import APIRouter
from services.chat_service import chat_with_gpt

router = APIRouter()

@router.post("/chat")
async def chat_route(prompt: str):
    return await chat_with_gpt(prompt)
