from fastapi import FastAPI
import pandas as pd
from src.predict import predict

app = FastAPI()

@app.post("/predict")
def get_prediction(data: dict):
    df = pd.DataFrame([data])
    result = predict(df)
    return {"prediction": result.tolist()}
