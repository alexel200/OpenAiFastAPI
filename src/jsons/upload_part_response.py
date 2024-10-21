from typing import Any

from pydantic import BaseModel
from pydantic_core.core_schema import none_schema


class UploadPartResponse(BaseModel):
    id: str | None = None
    object: str | None = None
    created_at: int | None = None
    upload_id: str | None = None

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> 'UploadPartResponse':
        return cls(
            id=data.get('id', ''),
            object=data.get('object', ''),
            created_at=data.get('created_at', 0),
            upload_id=data.get('upload_id', '')
        )
