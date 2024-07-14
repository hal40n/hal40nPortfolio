import sys
import os
from dotenv import load_dotenv

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from getPhotos import get_photos

load_dotenv()

app = FastAPI()

@app.get("/photos")
def show_photos():
    instagram_business_account_id = os.getenv('INSTAGRAM_BUSINESS_ACCOUNT_ID')
    instagram_access_token = os.getenv('INSTAGRAM_ACCESS_TOKEN')

    if not instagram_business_account_id or not instagram_access_token:
        raise HTTPException(status_code=400, detail="Missing Instagram credentials")

    try:
        photos = get_photos(instagram_business_account_id, instagram_access_token)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return JSONResponse(content=photos)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
