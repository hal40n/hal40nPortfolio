#!/bin/sh

# getArticleアプリケーションをバックグラウンドで実行
uvicorn getArticle.main:app --host 0.0.0.0 --port 8001 &

# getPhotoアプリケーションをフォアグラウンドで実行
uvicorn getPhoto.main:app --host 0.0.0.0 --port 8002
