import openai
import os

# APIキーの設定
openai.api_key = os.getenv("OPENAI_API_KEY")

async def chat_with_gpt(prompt: str):
    response = openai.Completion.create(
        engine="text-davinci-003",  # 使用するモデル
        prompt=prompt,
        max_tokens=100
    )
    return {"response": response.choices[0].text.strip()}
