from fastapi import FastAPI

app = FastAPI()

from fastapi import FastAPI
from routers import chat
from routers import wave

app = FastAPI()

# ルーターを追加
app.include_router(chat.router)
app.include_router(wave.router)
