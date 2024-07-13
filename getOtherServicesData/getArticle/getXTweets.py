import os
import requests
import json
from fastapi import HTTPException

bearer_token = os.getenv('BEARER_TOKEN')
url = "https://api.twitter.com/2/tweets/search/recent"
query_params = {
    'query': 'from:TwitterDev -is:retweet',
    'tweet.fields': 'created_at'
}

def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

def get_x_tweets():
    try:
        x_response = connect_to_endpoint(url, query_params)
        tweets = []

        for tweet in x_response.get('data', []):
            tweets.append({
                'url': f"https://twitter.com/twitter/status/{tweet['id']}",
                'created': tweet['created_at']
            })

        return tweets

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e)) from e