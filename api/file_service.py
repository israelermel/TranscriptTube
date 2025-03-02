import os
import zipfile
from typing import List


class FileService:
    @staticmethod
    def create_zip(files: List[str], zip_filename: str) -> str:
        """Cria um arquivo ZIP contendo vários arquivos."""
        with zipfile.ZipFile(zip_filename, 'w') as zipf:
            for file in files:
                zipf.write(file)

        return zip_filename

    @staticmethod
    def cleanup_files(files: List[str]) -> None:
        """Remove arquivos temporários."""
        for file in files:
            if os.path.exists(file):
                os.remove(file)