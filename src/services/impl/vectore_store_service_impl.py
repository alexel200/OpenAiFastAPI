import json
import os
import time

import requests
from dotenv import load_dotenv

from src.jsons.vectore_store_file_attach_response import VectorStoreFileAttachResponse
from src.services.vector_store_service_interface import VectorStoreServiceInterface

load_dotenv(verbose=True)

API_URL = os.getenv("API_URL")
API_KEY = os.getenv("API_KEY")
class VectorStoreServiceImpl(VectorStoreServiceInterface):

    def attach_file(self, vector_id: str, file_id: str, attempt=0, initial_seconds = 0 )->VectorStoreFileAttachResponse:
        if attempt == 3:
            raise Exception("Couldn't create upload")

        headers = {'Content-Type': 'application/json', "OpenAI-Beta": "assistants=v2", "Authorization": "Bearer " + API_KEY}
        url = API_URL + f"/vector_stores/{vector_id}/files"
        data = {
            'file_id': file_id,
        }
        data = json.dumps(data)
        response = requests.post(url, data=data, headers= headers)

        if response.status_code == requests.codes.ok:
            return VectorStoreFileAttachResponse().from_json(response.json())
        elif response.status_code == requests.codes.server_error:
            initial_seconds = initial_seconds + 2
            time.sleep(initial_seconds)
            self.attach_file(vector_id, file_id, attempt + 1, initial_seconds)
        else:
            raise Exception(response.json())

