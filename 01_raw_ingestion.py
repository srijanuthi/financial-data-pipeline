# Databricks notebook source
df=spark.table('creditcard')
display(df)

# COMMAND ----------

print("Raw row count:", df.count())
assert df.count()>0, 'No Raw Data Found'
print("Raw Data check passed")