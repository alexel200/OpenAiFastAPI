from typing import Any

from pydantic import BaseModel

class FileResponse(BaseModel):
    id: str | None
    object: str | None
    bytes: int | None
    created_at: int | None
    filename: str | None
    purpose: str | None

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> 'FileResponse':
        return cls(
            id=data.get('id', ''),
            object=data.get('object', ''),
            bytes=data.get('bytes', 0),
            created_at=data.get('created_at', 0),
            filename=data.get('filename', ''),
            purpose=data.get('purpose', '')
        )
