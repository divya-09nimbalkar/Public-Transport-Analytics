import pandas as pd
from src.preprocess import preprocess

def test_preprocess():
    df = pd.DataFrame({"date":["2020-01-01", None], "ridership":[100,200]})
    cleaned = preprocess(df)
    assert "date" in cleaned.columns
    assert cleaned.isnull().sum().sum() == 0
