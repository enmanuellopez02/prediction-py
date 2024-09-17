# Stock Price Prediction API

This project is a FastAPI application that predicts stock prices using the Prophet library. It reads historical stock prices from a CSV file and forecasts the next year's stock price.

## Installation

1. **Clone the repository**:
    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Create a virtual environment**:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Run the FastAPI application**:
    ```sh
    uvicorn main:app --reload
    ```

2. **Access the API documentation**:
    Open your browser and navigate to `http://127.0.0.1:8000/docs` to view the interactive API documentation provided by Swagger UI.

## Endpoints

### POST /predict/

This endpoint accepts a form parameter `prompt` and returns a prediction for the next year's stock price.

- **Request**:
    - `prompt`: A string form parameter (not used in the current implementation).

- **Response**:
    - `year`: The year for which the prediction is made.
    - `value`: The predicted stock price value.

Example request using `curl`:
```sh
curl -X 'POST' \
  'http://127.0.0.1:8000/predict/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'prompt=example'