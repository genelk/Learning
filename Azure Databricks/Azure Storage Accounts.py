from azure.storage.blob import BlobServiceClient

# Uploading files to Azure Blob Storage (like S3)
blob_service_client = BlobServiceClient.from_connection_string(conn_str)
blob_client = blob_service_client.get_blob_client(container="data", blob="file.csv")

with open("local_file.csv", "rb") as data:
    blob_client.upload_blob(data)
```

### **What Interviewers Would Ask:**

- "How do you authenticate to Azure services in production?" (Service principals, managed identities)
- "What's the difference between Azure Blob Storage and ADLS Gen2?"
- "How do you orchestrate data workflows in Azure?" (Data Factory, Synapse, Databricks Jobs)
- "Explain Azure resource groups and how you organize resources"

### **Beginner Project (1 Week):**
```
Build a simple Azure ETL pipeline:
1. Create free Azure account
2. Upload CSV to Azure Blob Storage
3. Create Azure Databricks workspace
4. Read data from Blob, transform with PySpark
5. Write to Azure SQL Database
6. Schedule with Azure Data Factory
