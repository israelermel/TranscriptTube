# api/file_service.py
import os
import zipfile
from typing import List


class FileService:
    @staticmethod
    def create_output_dir() -> str:
        """Cria e retorna o diretório de saída para os arquivos.

        Se estiver rodando em Docker, usa o diretório /app/downloads,
        caso contrário, usa o diretório atual.

        Returns:
            Caminho do diretório de saída
        """
        # Verifica se está rodando em ambiente Docker
        in_docker = os.path.exists('/.dockerenv')

        # Define o diretório de saída
        if in_docker:
            output_dir = "/app/downloads"
        else:
            output_dir = "downloads"

        # Cria o diretório se não existir
        os.makedirs(output_dir, exist_ok=True)

        return output_dir

    @staticmethod
    def create_zip(files: List[str], zip_name: str) -> str:
        """Cria um arquivo ZIP contendo vários arquivos.

        Args:
            files: Lista de caminhos de arquivos para incluir no ZIP
            zip_name: Nome do arquivo ZIP a ser criado

        Returns:
            Caminho completo do arquivo ZIP criado
        """
        # Cria o diretório de saída
        output_dir = FileService.create_output_dir()

        # Caminho completo para o arquivo ZIP
        zip_path = os.path.join(output_dir, zip_name)

        with zipfile.ZipFile(zip_path, 'w') as zipf:
            for file in files:
                # Adiciona apenas o nome do arquivo no ZIP, não o caminho completo
                zipf.write(file, os.path.basename(file))

        return zip_path

    @staticmethod
    def cleanup_files(files: List[str]) -> None:
        """Remove arquivos temporários.

        Args:
            files: Lista de caminhos de arquivos para remover
        """
        for file in files:
            if os.path.exists(file):
                try:
                    os.remove(file)
                except Exception as e:
                    print(f"Erro ao remover arquivo {file}: {str(e)}")

    @staticmethod
    def get_file_size(file_path: str) -> str:
        """Retorna o tamanho do arquivo em formato legível.

        Args:
            file_path: Caminho do arquivo

        Returns:
            Tamanho do arquivo formatado (KB, MB, etc.)
        """
        if not os.path.exists(file_path):
            return "0 B"

        size_bytes = os.path.getsize(file_path)

        # Converter para formato legível
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.2f} {unit}"
            size_bytes /= 1024.0

        return f"{size_bytes:.2f} TB"