import os
import requests

def get_photos(id, token):
    content = "{ caption,media_url,thumbnail_url,permalink}"

    url = f"https://graph.facebook.com/v20.0/{id}?fields=name,media{content}&access_token={token}"

    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()