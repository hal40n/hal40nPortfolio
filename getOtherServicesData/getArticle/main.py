from fastapi import FastAPI
from requests.auth import HTTPBasicAuth
import os
import json
from getQiitaArticles import *
from getHatenaArticles import *
from getXTweets import *


app = FastAPI()

@app.get("/articles")
def show_articles():
    hatena_id = os.getenv('HATENA_ID')
    hatena_api_key = os.getenv('HATENA_API_KEY')

    articles = {}
    hatena_articles = get_hatena_articles(hatena_id, hatena_api_key)
    qiita_articles = get_qiita_articles()
    x_tweets = get_x_tweets()

    articles = hatena_articles + qiita_articles + x_tweets

    sorted_articles = sorted(articles, key=lambda x: x['created'], reverse=True)

    return json.dump(sorted_articles, indent=4)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)