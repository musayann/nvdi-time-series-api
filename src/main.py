from fastapi import FastAPI
from src.ndvi.api import ndvi_router

app = FastAPI()

app.include_router(ndvi_router, prefix="/ndvi", tags=["NDVI"])