# Financial Transactions Data Pipeline

A personal data engineering project built to develop hands-on PySpark and Databricks skills.

## What this project does

Ingests a real credit card transactions dataset from Kaggle, applies PySpark 
transformations to clean and aggregate the data, and validates data quality 
at each stage — following a 3-layer Medallion architecture (Raw → Cleaned → Aggregated).

## Architecture 
Raw CSV (Kaggle)
↓
Raw Layer — Load into Databricks table, row count validation
↓
Cleaned Layer — Remove nulls, remove duplicates, data quality checks
↓
Aggregated Layer — Group by category, total amount per group
## Notebooks

| File | Description |
|------|-------------|
| 01_raw_ingestion.py | Loads raw CSV into Databricks, validates row count |
| 02_transformation.py | Cleans data, removes nulls & duplicates, runs quality checks, saves output |

## Sample Code

```python
# Load raw data
df = spark.table("transactions_raw")

# Clean and transform
df_clean = df.filter(df.amount > 0).dropDuplicates()

# Data quality checks
assert df_clean.count() > 0, "No data found!"
assert df_clean.filter(df_clean.amount.isNull()).count() == 0, "Null amounts found!"

# Validate row count didn't drop more than 50%
assert df_clean.count() >= df.count() * 0.5, "Too many rows dropped!"

# Save to cleaned layer
df_clean.write.mode("overwrite").saveAsTable("transactions_cleaned")
```

## Tools Used

- PySpark (Apache Spark)
- Databricks Community Edition
- Spark SQL
- Python
- GitHub

## Dataset

Credit card transactions dataset from Kaggle —
https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

## Author

**Srija Nuthi**  
Data Engineer at Accenture | Databricks Certified Data Engineer Associate  
[LinkedIn](https://www.linkedin.com/in/srija-nuthi-1091021b4) | [GitHub](https://github.com/srijanuthi)

