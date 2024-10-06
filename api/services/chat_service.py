import os
from openai import OpenAI
from fastapi import HTTPException

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def chat_with_gpt(prompt: str):
    try:
        print(f"Received prompt: {prompt}")  # 受け取ったプロンプトを出力
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        print(f"API Response: {response}")  # APIレスポンスを出力
        return {"response": response.choices[0].message.content}
    except Exception as e:
        print(f"OpenAI API error: {str(e)}")  # デバッグ用にエラーを出力
        raise HTTPException(status_code=500, detail=f"OpenAI API error: {str(e)}")
