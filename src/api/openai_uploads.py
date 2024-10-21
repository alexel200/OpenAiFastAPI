from fastapi import APIRouter

from src.jsons.upload_cancel_response import UploadCancelResponse
from src.jsons.upload_complete_response import UploadCompleteResponse
from src.jsons.upload_response import UploadResponse
from src.services.impl.upload_service_impl import UploadServiceImpl

router = APIRouter()

# Dependency injection using Depends
def upload_service(): return UploadServiceImpl()

@router.post('/uploads/create-upload', response_model=UploadResponse, tags=['openai_uploads'])
async def create_upload(path: str, purpose:str) -> UploadResponse:
    return upload_service().create_upload(path, purpose)

@router.post('/uploads/{upload_id}/parts', response_model=str, tags=['openai_uploads'])
async def upload_parts(upload_id:str, path: str)->str:
    return upload_service().upload_file_parts(upload_id, path)

@router.post('/uploads/{upload_id}/complete', response_model=UploadCompleteResponse, tags=['openai_uploads'])
async def complete_upload(upload_id:str, file_part_ids: str) -> UploadCompleteResponse:
    return upload_service().complete_upload(upload_id, file_part_ids)

@router.post('/uploads/{uploadId}/cancel', response_model=UploadCancelResponse, tags=['openai_uploads'])
async def cancel_upload(upload_id: str)->UploadCancelResponse:
    return upload_service().cancel_upload(upload_id)