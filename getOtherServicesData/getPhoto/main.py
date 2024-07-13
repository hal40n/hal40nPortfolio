from fastapi import FastAPI
from requests.auth import HTTPBasicAuth
import os
import json
from getPhotos import *

app = FastAPI()

@app.get("/photos")
def show_photos():
    instagram_business_account_id = os.getenv('INSTAGRAM_BUSINESS_ACCOUNT_ID')
    instagram_access_token = os.getenv('INSTAGRAM_ACCESS_TOKEN')
    photos = get_photos(instagram_business_account_id, instagram_access_token)
    return json.dump(photos, indent=4)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)