from typing import overload

from src.models.file import File

class CreateUploadRequest:
    def __init__(self, file:File, purpose:str):
        self.__purpose: str = purpose
        self.__filename: str = file.filename
        self.__bytes:int = file.bytes
        self.__mime_type:str = file.mime_type

    @property
    def purpose(self) -> str:
        return self.__purpose

    @property
    def filename(self) -> str:
        return self.__filename

    @property
    def bytes(self) -> int:
        return self.__bytes

    @property
    def mime_type(self) -> str:
        return self.__mime_type

    def to_dict(self):
        return {
            "purpose": self.__purpose,
            "filename": self.__filename,
            "bytes": self.__bytes,
            "mime_type": self.__mime_type
        }