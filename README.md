# Python ETL Pipeline with Data Validation

## Overview
This project demonstrates a simple but realistic Python-based ETL
(Extract, Transform, Load) pipeline commonly used in analytics and
data engineering workflows.

The focus is on clean Python structure, data validation, and handling
real-world data issues rather than complex frameworks.

## Objectives
- Extract data from flat files
- Apply transformations using Python
- Validate data before loading
- Log pipeline steps and failures
- Demonstrate interview-ready ETL scenarios

## ETL Design
The pipeline is structured into clear stages:
- Extract: Read raw input data
- Transform: Clean and standardize data
- Load: Write validated data to an output destination

## Status
Project initialized. ETL components will be added incrementally.

## How to Run the Pipeline

1. Ensure Python and required libraries are installed.
2. Place raw input data in the `data/` directory.
3. Run the pipeline using:

```bash
python src/main.py

## Interview Scenarios

- If extraction fails, the pipeline logs the error and stops execution.
- If transformation removes invalid records, the changes are logged with row counts.
- If loading fails, no partial output is considered successful.
- Validation logic can be extended without changing extract or load steps.

