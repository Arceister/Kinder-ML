from fastapi import FastAPI
from Middlewares import cors

app = FastAPI(middleware=cors.cors_middleware)

@app.get("/")
def hit_api():
  return {
    "message": "Success"
  }