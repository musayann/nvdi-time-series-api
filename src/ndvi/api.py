from fastapi import APIRouter
from src.ndvi import schema, service

ndvi_router = APIRouter()


@ndvi_router.post("/timeseries")
def get_ndvi_timeseries(request: schema.NDVIRequestSchema):
    return service.get_ndvi_timeseries(request.coordinates, request.start_date.isoformat(), request.end_date.isoformat())