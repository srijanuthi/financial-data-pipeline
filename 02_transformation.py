# Databricks notebook source
df=spark.table('creditcard')



# COMMAND ----------

df_clean=df.filter(df.Amount>0).dropDuplicates()


# COMMAND ----------

assert df_clean.count()>0, 'No Data Found'
assert df_clean.filter(df_clean.Amount.isNull()).count() == 0, 'Null amounts found!'
null_count = df_clean.filter(df_clean.Amount.isNull()).count()
display(null_count)
print("Raw data count:",df.count())
print("cleaned data count:",df_clean.count())
assert df_clean.count()>0 , 'No Data Found After Cleaning!'
assert df_clean.count()>=df.count()*0.5,'Too many rows dropped during cleaning'
print("Data quality checks passed ✓")


# COMMAND ----------

df_clean.write.mode("overwrite").saveAsTable("Transactions_cleaned")
print("saved Transactions_cleaned")
