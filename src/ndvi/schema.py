from datetime import date
from pydantic import BaseModel as BaseSchema, conlist, model_validator
from typing import List

# Define a coordinate pair: [longitude, latitude]
Coordinate = conlist(float, min_length=2, max_length=2)

# A linear ring: list of coordinate pairs
LinearRing = List[Coordinate]


class NDVIRequestSchema(BaseSchema):
    start_date: date
    end_date: date
    coordinates: List[LinearRing]
    
    @model_validator(mode='before')
    def check_date_order(cls, values):
        start = values.get('start_date')
        end = values.get('end_date')
        if start and end and start >= end:
            raise ValueError('start_date must be earlier than end_date')
        return values