from fastapi import FastAPI
from app.api.v1.routes import router

app = FastAPI(title="E-Commerce Search Service")

@app.get("/")
def health():
    return {"status": "OK"}

app.include_router(router)
