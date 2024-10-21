import os

class FileUtils:
    @staticmethod
    def is_file(path: str) -> bool:
        return os.path.isfile(path)

    @staticmethod
    def get_mime_types(extension: str) -> str:
        match extension:
            case ".pdf":
                return "application/pdf"

            case _:
                raise Exception("File not supported")

    @staticmethod
    def chunk_file(path: str, chunk_size=64 * 1024 * 1024):
        if not FileUtils.is_file(path):
            raise FileNotFoundError

        file_size = os.path.getsize(path)
        chunks = []
        with open(path, 'rb') as file:
            chunk_number = 0
            while chunk_number * chunk_size <= file_size:
                chunk_data = file.read(chunk_size)
                chunks.append(chunk_data)
                chunk_number += 1

        return chunks