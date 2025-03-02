from fpdf import FPDF
import re
from typing import List, Optional
from models.data_models import Video


class PDFService:
    @staticmethod
    def create_pdf(video: Video) -> Optional[str]:
        """Cria um arquivo PDF com a transcrição."""
        if not video.transcript:
            return None

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

        filename = f"{safe_title}.pdf"
        pdf.output(filename)
        return filename