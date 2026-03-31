from fastapi import FastAPI
from app.routes import video, image, text

app = FastAPI()

app.include_router(video.router)
app.include_router(image.router)
app.include_router(text.router)

@app.get("/")
def home():
    return {"message": "DeepTrace API Running"}