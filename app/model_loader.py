import torch
import joblib

# Load once (global)
video_model = torch.load("app/models/video_model.pth", map_location="cpu")
video_model.eval()

image_model = torch.load("app/models/image_model.pth", map_location="cpu")
image_model.eval()

text_model = joblib.load("app/models/text_model.pkl")
text_model.eval()