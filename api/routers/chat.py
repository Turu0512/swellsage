from fastapi import APIRouter
from pydantic import BaseModel
from services.chat_service import chat_with_gpt

router = APIRouter()

# リクエストボディ用のPydanticモデルを定義
class PromptRequest(BaseModel):
    prompt: str

@router.post("/chat")
async def chat_route(prompt_request: PromptRequest):
    return await chat_with_gpt(prompt_request.prompt)
