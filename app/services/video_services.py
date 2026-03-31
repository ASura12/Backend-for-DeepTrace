import cv2
import torch
from app.model_loader import video_model

def preprocess_frame(frame):
    # Resize
    frame = cv2.resize(frame, (224, 224))

    # Normalize
    frame = frame / 255.0

    # Convert to tensor
    frame = torch.tensor(frame).permute(2, 0, 1).float()

    # Add batch dimension
    frame = frame.unsqueeze(0)

    return frame


def analyze_video(path):
    cap = cv2.VideoCapture(path)

    predictions = []
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 🔥 Frame Skipping (VERY IMPORTANT)
        if frame_count % 5 != 0:
            frame_count += 1
            continue

        frame = preprocess_frame(frame)

        with torch.no_grad():
            pred = video_model(frame)

        predictions.append(pred.item())
        frame_count += 1

    cap.release()

    # Avoid crash if no frames
    if len(predictions) == 0:
        return {"error": "No frames processed"}
    

    final_score = sum(predictions) / len(predictions)

    return {
    "fake_probability": final_score,
    "verdict": "Fake" if final_score > 0.5 else "Real"
}