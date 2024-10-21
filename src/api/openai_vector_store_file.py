from fastapi import APIRouter, Depends

from src.jsons.vectore_store_file_attach_response import VectorStoreFileAttachResponse
from src.services.impl.vectore_store_service_impl import VectorStoreServiceImpl
router = APIRouter()

def vector_store_service() -> VectorStoreServiceImpl:
    return VectorStoreServiceImpl()

@router.post('/vector_stores/{vector_store_id}/file', response_model=VectorStoreFileAttachResponse, tags=['openai_vector_store_files'])
async def vector_store_attach_file(vector_store_id: str, file_id: str, service: VectorStoreServiceImpl = Depends(vector_store_service)) -> VectorStoreFileAttachResponse:
    return service.attach_file(vector_id=vector_store_id, file_id=file_id)