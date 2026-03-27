from azure.storage.blob import BlobServiceClient

# Uploading files to Azure Blob Storage
blob_service_client = BlobServiceClient.from_connection_string(conn_str)
blob_client = blob_service_client.get_blob_client(container="data", blob="file.csv")

with open("local_file.csv", "rb") as data:
    blob_client.upload_blob(data)
