import openeo
from src.config import OPENEO_API_URL, OPENEO_CLIENT_ID, OPENEO_CLIENT_SECRET


def get_openeo_instance():
    connection = openeo.connect(url=OPENEO_API_URL)
    connection.authenticate_oidc_client_credentials(
        client_id=OPENEO_CLIENT_ID,
        client_secret=OPENEO_CLIENT_SECRET
    )
    return connection


def load_fields(coordinates: dict):
    return {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": coordinates
                }
            }
        ]
    }


def get_ndvi_timeseries(coordinates: dict, start_date: str, end_date: str):
    connection = get_openeo_instance()
    fields = load_fields(coordinates)
    s2cube = connection.load_collection(
        "SENTINEL2_L2A",
        temporal_extent=[start_date, end_date],
        bands=["B04", "B08"],
    )

    red = s2cube.band("B04")
    nir = s2cube.band("B08")
    ndvi = (nir - red) / (nir + red)

    timeseries = ndvi.aggregate_spatial(geometries=fields, reducer="mean")

    # job = timeseries.execute(out_format="GeoJSON", title="NDVI timeseries")
    return timeseries.execute()
