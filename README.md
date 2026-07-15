# Financial Transactions Data Pipeline

A personal data engineering project built to develop hands-on pipeline skills.

## What this project does
Ingests a real financial transactions dataset from Kaggle, applies PySpark 
transformations to clean and aggregate the data, and validates data quality 
at each stage — following a 3-layer Medallion architecture (Raw → Cleaned → Aggregated).

## Architecture
Raw CSV (Kaggle) → Databricks Table (Raw layer) → Cleaned Table (CDZ layer) → Aggregated Table (PDZ layer)

## Notebooks
- 01_raw_ingestion — loads raw CSV data into Databricks, runs row count validation
- 02_transformation — cleans data, removes nulls and duplicates, saves cleaned output, runs data quality checks

## Tools used
- PySpark (Apache Spark)
- Databricks Community Edition
- SQL
- Python

## Dataset
Credit card transactions dataset from Kaggle (public domain)

## Author
Srija Nuthi — Data Engineer at Accenture | Databricks Certified Data Engineer Associate
