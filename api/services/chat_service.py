import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# APIキーの設定

async def chat_with_gpt(prompt: str):
    response = client.chat.completions.create(model="gpt-3.5-turbo",  # ChatGPTモデルを指定
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ])
    # ChatGPTの応答を返す
    return {"response": response.choices[0].message.content}
