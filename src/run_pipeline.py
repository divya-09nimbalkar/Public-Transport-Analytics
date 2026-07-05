from src.data_loader import load_raw_data
from src.preprocess import preprocess

def main():
    df = load_raw_data("data/raw/ridership.csv")
    df_clean = preprocess(df)
    print(df_clean.head())

if __name__ == "__main__":
    main()
