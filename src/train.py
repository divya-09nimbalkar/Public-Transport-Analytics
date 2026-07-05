import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

def train_model():
    # Load data
    df = pd.read_csv("data/raw/ridership.csv")

    # Separate features and target
    X = df.drop(columns=["passengers"])
    y = df["passengers"]

    # Define preprocessing:
    # - Convert date to numeric (e.g., day of year)
    X["date"] = pd.to_datetime(X["date"])
    X["day_of_year"] = X["date"].dt.dayofyear
    X = X.drop(columns=["date"])

    # Identify categorical columns
    categorical_cols = ["line", "station"]

    # Preprocessor: one-hot encode categorical columns
    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols)
        ],
        remainder="passthrough"  # keep numeric columns
    )

    # Build pipeline: preprocessing + regression
    model = Pipeline(steps=[
        ("preprocessor", preprocessor),
        ("regressor", LinearRegression())
    ])

    # Train
    model.fit(X, y)

    # Save model
    joblib.dump(model, "models/ridership_model.pkl")
    print("✅ Model trained and saved to models/ridership_model.pkl")

if __name__ == "__main__":
    train_model()
