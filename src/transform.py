import pandas as pd
import logging

def transform_customers(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and transform customer data.
    """
    logging.info("Starting customer data transformation")

    initial_count = len(df)

    # Remove duplicate customer records
    df = df.drop_duplicates(subset=["customer_id"])
    logging.info(f"Removed duplicates. Rows now: {len(df)}")

    # Handle missing email addresses
    missing_email_count = df["email"].isna().sum()
    df = df.dropna(subset=["email"])
    logging.info(f"Removed rows with missing email: {missing_email_count}")

    # Convert created_date to datetime, drop invalid dates
    df["created_date"] = pd.to_datetime(df["created_date"], errors="coerce")
    invalid_dates = df["created_date"].isna().sum()
    df = df.dropna(subset=["created_date"])
    logging.info(f"Removed rows with invalid dates: {invalid_dates}")

    final_count = len(df)
    logging.info(f"Transformation completed. Rows before: {initial_count}, Rows after: {final_count}")

    return df
