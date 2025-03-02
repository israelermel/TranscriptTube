# api/pdf_service.py
from fpdf import FPDF
import re
import os
from typing import List, Optional
from models.data_models import Video


class PDFService:
    @staticmethod
    def create_output_dir() -> str:
        """Cria e retorna o diretório de saída para os arquivos PDF.

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
    def create_pdf(video: Video) -> Optional[str]:
        """Cria um arquivo PDF com a transcrição.

        Args:
            video: Objeto Video contendo a transcrição

        Returns:
            Caminho do arquivo PDF criado ou None se falhar
        """
        if not video.transcript:
            return None

        # Cria o diretório de saída
        output_dir = PDFService.create_output_dir()

        # Sanitiza o título para usar como nome de arquivo
        safe_title = re.sub(r'[\\/*?:"<>|]', "", video.title)
        safe_title = safe_title[:100]  # Limita o tamanho do título

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Adiciona o título
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(200, 10, txt=video.title[:70], ln=True, align='C')
        pdf.ln(10)

        # Adiciona o ID do vídeo e o idioma utilizado
        pdf.set_font("Arial", 'I', 10)
        pdf.cell(200, 10, txt=f"Video ID: {video.id}", ln=True, align='L')
        if hasattr(video, 'language_used') and video.language_used:
            pdf.cell(200, 10, txt=f"Idioma: {video.language_used}", ln=True, align='L')
        pdf.ln(5)

        # Adiciona a transcrição
        pdf.set_font("Arial", size=12)

        full_text = ""
        for item in video.transcript:
            full_text += item.text + " "

        # Quebra o texto em linhas para caber na página
        lines = []
        words = full_text.split()
        current_line = ""

        for word in words:
            test_line = current_line + " " + word if current_line else word
            if pdf.get_string_width(test_line) < 180:  # Largura da página menos margens
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word

        if current_line:
            lines.append(current_line)

        for line in lines:
            pdf.multi_cell(0, 10, txt=line)

        # Adiciona informações de rodapé
        pdf.set_y(-30)
        pdf.set_font("Arial", 'I', 8)
        pdf.cell(0, 10, txt="Gerado por TranscriptTube - https://github.com/israelermel/TranscriptTube", 0, 0, 'C')

        # Gera o arquivo com caminho completo
        filename = os.path.join(output_dir, f"{safe_title}.pdf")
        pdf.output(filename)

        return filename