import pandas as pd
from src.train import train_model

def test_train_model(tmp_path):
    df = pd.DataFrame({"feature":[1,2,3], "ridership":[10,20,30]})
    model = train_model(df)
    assert model is not None
