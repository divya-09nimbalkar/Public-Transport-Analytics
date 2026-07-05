import pandas as pd
from src.data_loader import load_raw_data

def test_load_raw_data(tmp_path):
    file = tmp_path / "test.csv"
    pd.DataFrame({"a":[1,2]}).to_csv(file, index=False)
    df = load_raw_data(file)
    assert not df.empty
