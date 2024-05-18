import os
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from pprint import pprint

subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]
connection_string = os.environ["AZURE_CONNECTION_STRING"]

blob_service_client = BlobServiceClient.from_connection_string(connection_string)

pprint(blob_service_client.get_account_information())

container_client = blob_service_client.get_container_client("html")

if not container_client:
    container_client = blob_service_client.create_container("html")

with open(os.path.join(os.getcwd(), 'dummy.html')) as file:
    blob_client = container_client.upload_blob('dummy.html', file.read(), overwrite=True)
    pprint(blob_client.url)

