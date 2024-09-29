# ベースイメージとしてPython 3.9を使用
FROM python:3.9-slim

# 作業ディレクトリを設定
WORKDIR /app

# 依存関係をコピーしてインストール
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのコードをコピー
COPY . .

# ポートを公開
EXPOSE 8000

# デフォルトのコマンドを設定（必要に応じて）
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
