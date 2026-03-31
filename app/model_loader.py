from pathlib import Path

import joblib
import torch

BASE_DIR = Path(__file__).resolve().parent
MODELS_DIR = BASE_DIR / "models"


def _validate_model_file(path: Path) -> None:
	if not path.exists():
		raise FileNotFoundError(f"Model file not found: {path}")
	if path.stat().st_size == 0:
		raise ValueError(f"Model file is empty (0 bytes): {path}")


def _load_torch_model(filename: str):
	path = MODELS_DIR / filename
	_validate_model_file(path)
	model = torch.load(path, map_location="cpu")
	if hasattr(model, "eval"):
		model.eval()
	return model


def _load_joblib_model(filename: str):
	path = MODELS_DIR / filename
	_validate_model_file(path)
	return joblib.load(path)


def _safe_load(loader, filename: str):
	try:
		return loader(filename), None
	except Exception as exc:
		return None, str(exc)


video_model, video_model_error = _safe_load(_load_torch_model, "video_model.pth")
image_model, image_model_error = _safe_load(_load_torch_model, "image_models.pth")
text_model, text_model_error = _safe_load(_load_joblib_model, "text_model.pkl")