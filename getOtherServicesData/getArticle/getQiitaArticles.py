from fastapi import HTTPException
import os
import requests

def get_qiita_token():
    qiita_access_token = os.getenv('QIITA_ACCESS_TOKEN')
    return qiita_access_token

def get_qiita_articles():
    try:

        qiita_access_token = get_qiita_token()

        headers = {
            'Authorization': f"Bearer {qiita_access_token}",
        }

        qiita_articles = []

        page = 1

        while True:
            url = f"https://qiita.com/api/v2/items?page={page}&per_page=100"
            response = requests.get(url, headers=headers)

            if response.status_code != 200:
                print('記事がありません')
                return None
            else:
                if not response.json():
                    break
                qiita_articles += response.json()
                page += 1

        qiita_article_details = [
            {
                "title": article['title'],
                "url": article['url'],
                "created": article['created_at'],
            }
            for article in qiita_articles
        ]
        return qiita_article_details

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e)) from e