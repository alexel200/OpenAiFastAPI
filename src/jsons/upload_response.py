from typing import Any

from pydantic import BaseModel

class UploadResponse(BaseModel):
    id:str|None = None
    object:str|None = None
    bytes:int|None = None
    created_at:int|None = None
    filename:str|None = None
    purpose:str|None = None
    status:str|None = None
    expires_at:int|None = None

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> 'UploadResponse':
        return cls(
            id=data.get('id', ''),
            object=data.get('object', ''),
            bytes=data.get('bytes', 0),
            created_at=data.get('created_at', 0),
            filename=data.get('filename', ''),
            purpose=data.get('purpose', ''),
            status=data.get('status', ''),
            expires_at=data.get('expires_at', 0)
        )