from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data

def run_pipeline():
    print("Starting ETL Pipeline")
    
    df = extract_data()
    print(f"Extracted {len(df)} rows")

    df = transform_data(df)
    print(f"Transformed dataframe with {df.shape[1]} columns")

    load_data(df)
    print("ETL Pipeline completed successfully!")

if __name__ == "__main__":
    run_pipeline()
