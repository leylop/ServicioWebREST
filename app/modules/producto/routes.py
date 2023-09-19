import json
import os
from flask import Blueprint, jsonify, request
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

import app.modules.usuario.services as usuario_services

usuario_blueprint = Blueprint('usuario', __name__)

CONNECTION_STRING = os.environ.get("CONNECTION_STRING")
CONTAINER_NAME = os.environ.get("CONTAINER_NAME")
BLOB_NAME = "123456.json"

@usuario_blueprint.route('/usuario', methods=['POST'])
def send_request():
    blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
    container_client = blob_service_client.get_container_client(CONTAINER_NAME)
    blob_client = container_client.get_blob_client(blob=BLOB_NAME)
    blob_content = blob_client.download_blob().readall()

    data = json.loads(blob_content)

    response_data = {
        "mensaje": "Usuario actualizado con éxito",
        "data": data
    }
    return usuario_services.emulate_and_save_data(jsonify(response_data))
