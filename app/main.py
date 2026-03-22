from fastapi import FastAPI
from app.api.routes import router


app = FastAPI(
    title="Bills General OCR",
    version="1.0"
)

@app.get("/")
async def root():
    return {"message": "welcome to Bills OCR"}