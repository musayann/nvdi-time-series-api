from fastapi import FastAPI

from src import schema, service

app = FastAPI()



@app.post("/ndvi/timeseries")
def get_ndvi_timeseries(request: schema.NDVIRequestSchema):
    return service.get_ndvi_timeseries(request.coordinates, request.start_date.isoformat(), request.end_date.isoformat())