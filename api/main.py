from fastapi import FastAPI

app = FastAPI()

from fastapi import FastAPI
from routers import chat

app = FastAPI()

# ルーターを追加
app.include_router(chat.router)
