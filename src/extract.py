import pandas as pd
import logging
from pathlib import Path

# Configure basic logging
logging.basicConfig(
    filename="logs/etl.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def extract_customers(file_path: str) -> pd.DataFrame:
    """
    Extract customer data from a CSV file.
    """
    logging.info(f"Starting data extraction from {file_path}")

    df = pd.read_csv(file_path)

    logging.info(f"Extraction completed. Rows extracted: {len(df)}")
    return df


if __name__ == "__main__":
    data_path = Path("data/raw_customers.csv")
    customers_df = extract_customers(data_path)
    print(customers_df.head())
