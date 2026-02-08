import pandas as pd
import logging
from pathlib import Path

def load_customers(df: pd.DataFrame, output_path: str) -> None:
    """
    Load cleaned customer data to a CSV file.
    """
    logging.info(f"Starting data load to {output_path}")

    output_file = Path(output_path)
    df.to_csv(output_file, index=False)

    logging.info(f"Data load completed. Rows loaded: {len(df)}")


if __name__ == "__main__":
    print("Load module ready.")
