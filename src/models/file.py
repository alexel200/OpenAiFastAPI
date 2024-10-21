from src.utils.file_utils import FileUtils
import os

class File:
    def __init__(self):
        self.__path: str | None = None
        self.__bytes: int | None = None
        self.__filename: str | None = None
        self.__extension: str | None = None
        self.__mimeType: str | None = None

    @property
    def path(self):
        return self.__path

    @property
    def bytes(self) -> int:
        return self.__bytes

    @property
    def filename(self) -> str:
        return self.__filename

    @property
    def extension(self) -> str:
        return self.__extension

    @property
    def mime_type(self) -> str:
        return self.__mimeType

    def load_data(self, path: str):
        if not FileUtils.is_file(path):
            raise FileNotFoundError

        self.__path = path
        self.__bytes = os.path.getsize(path)
        self.__filename = os.path.basename(path)
        self.__extension = os.path.splitext(path)[1]
        self.__mimeType = FileUtils.get_mime_types(self.__extension.lower())
        return self


