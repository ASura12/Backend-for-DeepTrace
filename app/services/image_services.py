import cv2
import torch
from app.model_loader import image_model

def preprocess_image(path):
    img = cv2.imread(path)

    # Resize
    img = cv2.resize(img, (224, 224))

    # Normalize (0–1)
    img = img / 255.0

    # Convert to tensor
    img = torch.tensor(img).permute(2, 0, 1).float()

    # Add batch dimension
    img = img.unsqueeze(0)

    return img


def analyze_image(path):
    img = preprocess_image(path)

    with torch.no_grad():
        pred = image_model(img)

    return {
        "fake_probability": float(pred)
    }