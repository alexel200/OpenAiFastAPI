from typing import Any, Optional

from src.jsons import upload_response
from src.jsons.FileResponse import FileResponse

class UploadCompleteResponse(upload_response.UploadResponse):
        file: Optional[FileResponse] | None = None

        @classmethod
        def from_json(cls, data: dict[str, Any]) -> 'UploadCompleteResponse':
                parent_obj = super().from_json(data)
                file_data = data.get('file')
                file_obj = FileResponse.from_json(file_data) if file_data else None
                parent_dict = parent_obj.dict()
                parent_dict.pop('file', None)  # Ensure file is removed if it exists
                return cls(
                        **parent_dict,
                        file=file_obj
                )