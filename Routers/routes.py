from fastapi import APIRouter

router = APIRouter()

router.get("/")
async def hit_api():
  return {
    "message": "Success"
  }