import os
from fastapi import HTTPException
from services.wave_service import fetch_wave_data
from services.chat_service import chat_with_gpt

async def fetch_wave_and_chat(point: str):
    try:
        # 波情報を取得
        wave_data = await fetch_wave_data(point)

        # 環境変数からポイントの特徴を取得
        features = os.getenv(f"{point.upper()}_FEATURES", "特徴情報がありません。")

        # ChatGPTに送信するメッセージを準備
        message = f"ポイント名: {point}\n特徴: {features}\n波情報: {wave_data}"

        # メッセージをChatGPTに送信
        chat_response = await chat_with_gpt(point, features, message)

        return chat_response
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
