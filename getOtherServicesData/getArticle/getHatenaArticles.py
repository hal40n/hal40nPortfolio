import os
from dotenv import load_dotenv
import requests
from requests.auth import HTTPBasicAuth
from fastapi import HTTPException
import xmltodict

load_dotenv()

def generate_url(level, id):
    base_url = "https://blog.hatena.ne.jp"
    if level == "primary":
        hatena_blog_id = os.getenv('HATENA_BLOG_ID_PRIMARY')
    elif level == "secondary":
        hatena_blog_id = os.getenv('HATENA_BLOG_ID_SECONDARY')
    hatena_blog_url = f"{base_url}/{id}/{hatena_blog_id}.hatenablog.com"
    return hatena_blog_url

def get_hatena_articles(hatena_id, hatena_api_key):
    try:

        auth = HTTPBasicAuth(hatena_id, hatena_api_key)

        hatena_blog_primary_url = generate_url("primary", hatena_id)
        hatena_response_primary = requests.get(hatena_blog_primary_url, auth=auth)

        hatena_blog_secondary_url = generate_url("secondary", hatena_id)
        hatena_response_secondary = requests.get(hatena_blog_secondary_url, auth=auth)

        if hatena_response_primary.status_code != 200 and hatena_response_secondary.status_code != 200:
            raise HTTPException(status_code=404, detail="No articles found")

        articles = []

        if hatena_response_primary.status_code == 200:
            primary_data = xmltodict.parse(hatena_response_primary.text)
            if 'feed' in primary_data and 'entry' in primary_data['feed']:
                for entry in primary_data['feed']['entry']:
                    articles.append({
                        'url': entry['link']['@href'],
                        'created': entry['published']
                    })

        if hatena_response_secondary.status_code == 200:
            secondary_data = xmltodict.parse(hatena_response_secondary.text)
            if 'feed' in secondary_data and 'entry' in secondary_data['feed']:
                for entry in secondary_data['feed']['entry']:
                    articles.append({
                        'url': entry['link']['@href'],
                        'created': entry['published']
                    })

        return articles

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
