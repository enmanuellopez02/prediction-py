from fastapi import FastAPI, UploadFile, File, Form
from pydantic import BaseModel
import pandas as pd
from prophet import Prophet

# Inicializamos la app de FastAPI
app = FastAPI()

# Definimos la estructura de la respuesta
class PredictionResult(BaseModel):
    year: str
    value: float

@app.post("/predict/")
async def predict(prompt: str = Form(...)) -> dict:
    # Leer el archivo CSV
    df = pd.read_csv('data/stock_prices.csv')

    # Preparar el DataFrame para Prophet
    df.rename(columns={'year': 'ds', 'value': 'y'}, inplace=True)
    
    # Inicializar el modelo Prophet
    model = Prophet()
    model.fit(df)

    # Hacer una predicción para el próximo año
    future = pd.DataFrame({'ds': [str(int(df['ds'].max()) + 1)]})
    forecast = model.predict(future)
    
    # Obtener el valor pronosticado
    predicted_value = int(forecast['yhat'].iloc[0])
    last_year = int(df['ds'].max()) + 1

    # Estructuramos la respuesta final
    return {
        "prompt": prompt,
        "result": [{"year": str(int(year)), "value": int(value)} for year, value in zip(df['ds'], df['y'])] + [{"year": str(last_year), "value": predicted_value}],
        "prediction_text": f"Predicción para el año {last_year}: {predicted_value:.0f}"
    }

# Para correr la aplicación utiliza `uvicorn`:
# uvicorn main:app --reload
