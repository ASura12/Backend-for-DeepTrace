from fastapi import APIRouter, UploadFile
from app.services.video_service import analyze_video

router = APIRouter()

@router.post("/video")
async def video_detect(file: UploadFile):
    path = f"data/{file.filename}"

    # Save video
    with open(path, "wb") as f:
        f.write(await file.read())

    result = analyze_video(path)

    return result