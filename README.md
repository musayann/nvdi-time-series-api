# NDVI Time Series API

This FastAPI project provides an API endpoint to compute NDVI time series over a geographic area using Sentinel-2 data via the OpenEO API.

## Features

- Accepts a polygon and date range as input
- Computes NDVI using Sentinel-2 (L2A) bands B04 and B08
- Aggregates results spatially using the mean reducer
- Returns NDVI time series data as GeoJSON or JSON

---

## API Reference

### `POST /ndvi/timeseries`

Request the NDVI time series for a specified polygon and date range.

#### Request Body

```json
{
  "start_date": "2020-06-01",
  "end_date": "2020-06-30",
  "coordinates": [
    [
      [5.055945487931457, 51.222709834076504],
      [5.064972484168688, 51.221122565090525],
      [5.067474954083448, 51.218249806779134],
      [5.064827929485983, 51.21689628072789],
      [5.05917785594747, 51.217191909908095],
      [5.053553857094518, 51.21807492332223],
      [5.055945487931457, 51.222709834076504]
    ]
  ]
}
```

## Project Structure

```
├── src/
│   ├── ndvi/
│   │   ├── api.py           # FastAPI route for NDVI endpoint
│   │   ├── schema.py        # Pydantic request schema
│   │   └── service.py       # NDVI processing logic
│   ├── utils/
│   │   └── env_loader.py    # Utility to load environment variables
│   ├── config.py            # OpenEO configuration settings
│   └── main.py              # FastAPI entry point
├── .env.sample              # Sample environment variables
├── requirements.txt         # Python dependencies
```

## Setup

### Prerequisites

- Python 3.8+
- `fastapi[all]` and other dependencies listed in `requirements.txt`

### Installation

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### Configuration

Create a `.env` file based on the provided sample:

#### `.env.sample`

```env
OPENEO_API_URL="openeo.dataspace.copernicus.eu"
OPENEO_CLIENT_ID="CLIENT_ID_PLACEHOLDER"
OPENEO_CLIENT_SECRET="CLIENT_SECRET_PLACEHOLDER"
```

Rename it to `.env` and replace placeholder values with your actual OpenEO credentials.

---

## Running the API

Start the FastAPI development server:

```bash
fastapi dev src/main.py
```

Open your browser at: [http://localhost:8000/docs](http://localhost:8000/docs) to view and test the API.

See the interactive API documentation at: [http://localhost:8000/docs](http://localhost:8000/docs)