from fastapi import FastAPI
from app.api.router import api_router


app = FastAPI(
    title="Bills General OCR",
    version="1.0"
)

app.include_router(api_router)

@app.get("/")
async def root():
    return {"message": "welcome to Bills OCR"}