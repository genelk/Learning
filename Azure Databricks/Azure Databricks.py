# You've used Databricks on AWS - Azure Databricks is similar but with Azure-specific integrations
# Creating a cluster, running notebooks, connecting to Azure storage

# Example: Reading from Azure Data Lake Storage (ADLS)
df = spark.read.format("delta") \
    .load("abfss://container@storageaccount.dfs.core.windows.net/path/to/data")

# Writing to Azure SQL Database
df.write \
    .format("jdbc") \
    .option("url", "jdbc:sqlserver://server.database.windows.net:1433;database=mydb") \
    .option("dbtable", "my_table") \
    .save()
