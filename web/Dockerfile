# ベースイメージとしてUbuntuを使用
FROM ubuntu:20.04

# 必要なパッケージをインストール
RUN apt-get update && apt-get install -y \
    curl \
    git \
    unzip \
    xz-utils \
    zip \
    libglu1-mesa

# Flutterのバージョンを指定
ENV FLUTTER_VERSION=3.7.7

# Flutterをダウンロードして展開
RUN git clone -b ${FLUTTER_VERSION} https://github.com/flutter/flutter.git /usr/local/flutter

# 環境変数の設定
ENV PATH="/usr/local/flutter/bin:/usr/local/flutter/bin/cache/dart-sdk/bin:${PATH}"

# Flutterの依存関係を取得
RUN flutter doctor

# 非ルートユーザーを作成
RUN useradd -ms /bin/bash flutteruser

# Flutterディレクトリの所有権を変更
RUN chown -R flutteruser:flutteruser /usr/local/flutter

# 作業ディレクトリを設定
WORKDIR /app

# アプリケーションコードをコピー
COPY . /app

# アプリケーションディレクトリの所有権を変更
RUN chown -R flutteruser:flutteruser /app

# ユーザーを切り替え
USER flutteruser

# 依存関係を取得
RUN flutter pub get

# ポートを公開
EXPOSE 8080

# アプリケーションを起動
CMD ["flutter", "run", "-d", "web-server", "--web-port=8080", "--web-hostname=0.0.0.0"]
