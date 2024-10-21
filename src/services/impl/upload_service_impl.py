import json
import os
import time

import requests
from dotenv import load_dotenv

from src.jsons.create_upload_request import CreateUploadRequest
from src.jsons.upload_cancel_response import UploadCancelResponse
from src.jsons.upload_complete_response import UploadCompleteResponse
from src.jsons.upload_part_response import UploadPartResponse
from src.jsons.upload_response import UploadResponse
from src.models.file import File
from src.services.upload_service_interface import UploadServiceInterface
from src.utils.file_utils import FileUtils

load_dotenv(verbose=True)

API_URL = os.getenv("API_URL")
API_KEY = os.getenv("API_KEY")
class UploadServiceImpl(UploadServiceInterface):

    def create_upload(self, file_path: str, purpose: str, attempt = 0, initial_seconds = 0) -> UploadResponse:
        if attempt == 3:
            raise Exception("Couldn't create upload")

        file = File().load_data(file_path)
        upload_request = json.dumps(CreateUploadRequest(file, purpose).to_dict())
        headers = {'Content-Type': 'application/json', "Authorization": "Bearer " + API_KEY}
        url = API_URL + "/uploads"

        response = requests.post(url, data=upload_request, headers= headers)
        if response.status_code == requests.codes.ok:
            return UploadResponse().from_json(response.json())
        elif response.status_code == requests.codes.server_error:
            initial_seconds = initial_seconds + 2
            time.sleep(initial_seconds)
            self.create_upload(file_path, purpose, attempt + 1, initial_seconds)
        else:
            raise Exception(response.json())

    def cancel_upload(self, upload_id: str, attempt = 0, initial_seconds = 0):
        if attempt == 3:
            raise Exception("Couldn't create upload")

        headers = {'Content-Type': 'application/json', "Authorization": "Bearer " + API_KEY}
        url = API_URL + f"/uploads/{upload_id}/cancel"

        response = requests.post(url, headers=headers)

        if response.status_code == requests.codes.ok:
            return UploadCancelResponse().from_json(response.json())
        elif response.status_code == requests.codes.server_error:
            initial_seconds = initial_seconds + 2
            time.sleep(initial_seconds)
            self.cancel_upload(upload_id, attempt + 1, initial_seconds)
        else:
            raise Exception(response.json())

    def upload_file_parts(self, upload_id, path)-> str:
        if not FileUtils.is_file(path):
            raise Exception(path)
        file_parts_id = []
        chunks = FileUtils.chunk_file(path)
        headers = {"Authorization": "Bearer " + API_KEY}
        url = API_URL + f"/uploads/{upload_id}/parts"

        for i, chunk in enumerate(chunks):
            file = {
                'data': (f'chunk{i}', chunk)
            }
            upload_response = self.__perform_part_file_upload(url, headers, file)
            file_parts_id.append(upload_response.id)
        return json.dumps(file_parts_id)

    def __perform_part_file_upload(self, url, headers, file, attempt = 0, initial_seconds = 0)->UploadPartResponse:
        if attempt == 3:
            raise Exception("Couldn't upload part")

        upload_response = UploadPartResponse()
        response = requests.post(url, files=file, headers=headers)

        if response.status_code == requests.codes.ok:
            upload_response = UploadPartResponse().from_json(response.json())
        elif response.status_code == requests.codes.server_error:
            initial_seconds = initial_seconds + 2
            time.sleep(initial_seconds)
            upload_response = self.__perform_part_file_upload(url, headers, file, attempt + 1, initial_seconds)
        return upload_response

    def complete_upload(self, upload_id, file_part_ids, attempt = 0, initial_seconds = 0) -> UploadCompleteResponse:
        if attempt == 3:
            raise Exception("Couldn't complete upload")

        url = API_URL + f"/uploads/{upload_id}/complete"
        file_part_ids = json.loads(file_part_ids)
        headers = {'Content-Type': 'application/json', "Authorization": "Bearer " + API_KEY}
        data = json.dumps({"part_ids": file_part_ids})

        response = requests.post(url, data=data, headers=headers)

        if response.status_code == requests.codes.ok:
            return UploadCompleteResponse().from_json(response.json())
        elif response.status_code == requests.codes.server_error:
            initial_seconds = initial_seconds + 2
            time.sleep(initial_seconds)
            self.complete_upload(upload_id, json.dumps(file_part_ids), attempt + 1, initial_seconds)

