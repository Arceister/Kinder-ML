from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hit_api():
  return {
    "message": "Success"
  }