import logging
from pathlib import Path

from extract import extract_customers
from transform import transform_customers
from load import load_customers

# Configure logging (shared across pipeline)
logging.basicConfig(
    filename="logs/etl.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_pipeline():
    """
    Run the end-to-end ETL pipeline.
    """
    logging.info("ETL pipeline started")

    raw_data_path = Path("data/raw_customers.csv")
    output_data_path = Path("data/clean_customers.csv")

    # Extract
    customers_df = extract_customers(raw_data_path)

    # Transform
    cleaned_df = transform_customers(customers_df)

    # Load
    load_customers(cleaned_df, output_data_path)

    logging.info("ETL pipeline completed successfully")


if __name__ == "__main__":
    run_pipeline()
