import json
import os
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

# Obtener la conexión y el nombre del contenedor
CONNECTION_STRING = os.environ.get('CONNECTION_STRING')
CONTAINER_NAME = os.environ.get('CONTAINER_NAME')  # Reemplaza con el nombre de tu contenedor

def emulate_and_save_data(data,blob_name):

    # Convertir el diccionario a una cadena JSON
    data_str = json.dumps(data)

    # Crear un cliente para el Blob Service
    blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
    
    # Crear un cliente para el contenedor
    container_client = blob_service_client.get_container_client(CONTAINER_NAME)
    
    # Crear un cliente para el blob específico
    blob_name = "output/"+blob_name+".json"  # Puedes cambiar el nombre si lo deseas
    blob_client = container_client.get_blob_client(blob=blob_name)
    
    # Subir la cadena JSON al blob
    blob_client.upload_blob(data_str, overwrite=True)

    return "Data emulated and saved to blob successfully!"
