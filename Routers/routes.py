from fastapi import APIRouter
from Controllers import controller

router = APIRouter()

@router.get("/")
async def hit_api():
  return controller.api_hit_response()

@router.get("/predict")
def predict():
  return controller.predict_image()