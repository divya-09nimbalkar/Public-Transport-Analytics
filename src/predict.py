import joblib
import pandas as pd

def preprocess_for_prediction(df: pd.DataFrame) -> pd.DataFrame:
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"])
        df["day_of_year"] = df["date"].dt.dayofyear
        df = df.drop(columns=["date"])
    else:
        raise ValueError("Uploaded CSV must include a 'date' column.")

    return df

def predict(input_data: pd.DataFrame):
    model = joblib.load("models/ridership_model.pkl")
    df = preprocess_for_prediction(input_data)
    return model.predict(df)
