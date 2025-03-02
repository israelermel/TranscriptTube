# web/app.py
import streamlit as st
import time
import os
import sys

# Adiciona o diretório raiz ao sys.path para permitir importações relativas
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Agora que temos o caminho correto, podemos importar nossos módulos
try:
    from web.ui_components import UIComponents
    from api.youtube_service import YouTubeService
    from api.transcript_service import TranscriptService
    from api.pdf_service import PDFService
    from api.file_service import FileService
    from utils.url_utils import extract_video_id
except ImportError:
    # Tente importações absolutas se as relativas falharem
    from YoutubePDF.web.ui_components import UIComponents
    from YoutubePDF.api.youtube_service import YouTubeService
    from YoutubePDF.api.transcript_service import TranscriptService
    from YoutubePDF.api.pdf_service import PDFService
    from YoutubePDF.api.file_service import FileService
    from YoutubePDF.utils.url_utils import extract_video_id


class StreamlitApp:
    def __init__(self):
        self.ui = UIComponents
        self.youtube_service = YouTubeService
        self.transcript_service = TranscriptService
        self.pdf_service = PDFService
        self.file_service = FileService

    def run(self):
        """Executa a aplicação Streamlit."""
        self.ui.header()
        url = self.ui.input_section()

        if self.ui.action_button():
            self._process_url(url)

        # Limpar arquivos temporários
        if 'cleanup_file' in st.session_state and isinstance(st.session_state.cleanup_file, list):
            self.file_service.cleanup_files(st.session_state.cleanup_file)
            del st.session_state.cleanup_file

        self.ui.show_instructions()

    def _process_url(self, url: str):
        """Processa a URL fornecida pelo usuário."""
        if not url:
            self.ui.show_warning("Por favor, insira uma URL válida")
            return

        progress_bar, status_text = self.ui.progress_indicator()

        try:
            video_id = extract_video_id(url)

            if not video_id:
                self.ui.show_error("URL inválida. Por favor, verifique e tente novamente.")
                return

            # Verifica se é uma playlist
            if isinstance(video_id, tuple) and video_id[1] == 'playlist':
                self._process_playlist(video_id[0], progress_bar, status_text)
            else:
                self._process_video(video_id, progress_bar, status_text)

        except Exception as e:
            self.ui.show_error(f"Ocorreu um erro: {str(e)}")
            import traceback
            self.ui.show_error(traceback.format_exc())

    def _process_video(self, video_id: str, progress_bar, status_text):
        """Processa um único vídeo."""
        self.ui.update_progress(progress_bar, status_text, 0.3, "Processando vídeo...")

        # Obter detalhes do vídeo
        video = self.youtube_service.get_video_details(video_id)
        self.ui.update_progress(progress_bar, status_text, 0.5, f"Obtendo transcrição para: {video.title}")

        # Adicionar transcrição
        video = self.transcript_service.add_transcript_to_video(video)

        if video.transcript:
            self.ui.update_progress(progress_bar, status_text, 0.8, "Criando PDF...")

            # Criar PDF
            pdf_file = self.pdf_service.create_pdf(video)

            if pdf_file:
                self.ui.update_progress(progress_bar, status_text, 1.0, "Processamento concluído!")

                with open(pdf_file, "rb") as f:
                    self.ui.download_button(
                        label=f"Baixar transcrição: {video.title[:30]}...",
                        data=f,
                        file_name=pdf_file,
                        mime="application/pdf"
                    )

                # Marcar para limpeza posterior
                st.session_state.cleanup_file = [pdf_file]
            else:
                self.ui.show_error("Erro ao criar o arquivo PDF.")
        else:
            self.ui.update_progress(progress_bar, status_text, 1.0, "Processamento concluído!")
            self.ui.show_warning("Nenhuma transcrição disponível para este vídeo.")

    def _process_playlist(self, playlist_id: str, progress_bar, status_text):
        """Processa uma playlist completa."""
        self.ui.update_progress(progress_bar, status_text, 0.1, "Processando playlist...")

        # Obter informações da playlist
        playlist = self.youtube_service.get_playlist_details(playlist_id)
        total_videos = len(playlist.videos)

        if total_videos == 0:
            self.ui.show_error("Não foi possível encontrar vídeos na playlist ou a playlist está vazia.")
            return

        self.ui.show_info(f"Playlist: {playlist.title} - {total_videos} vídeos encontrados")
        pdf_files = []

        # Processar cada vídeo
        for i, video in enumerate(playlist.videos):
            progress = 0.1 + (0.8 * (i / total_videos))
            self.ui.update_progress(
                progress_bar,
                status_text,
                progress,
                f"Processando ({i + 1}/{total_videos}): {video.title}"
            )

            # Adicionar transcrição
            video = self.transcript_service.add_transcript_to_video(video)

            if video.transcript:
                # Criar PDF
                pdf_file = self.pdf_service.create_pdf(video)
                if pdf_file:
                    pdf_files.append(pdf_file)

            # Pequeno delay para não sobrecarregar a API
            time.sleep(0.5)

        # Criar ZIP com todos os PDFs
        if pdf_files:
            self.ui.update_progress(progress_bar, status_text, 0.9, "Criando arquivo ZIP...")

            zip_filename = f"{playlist.title[:50]}_transcricoes.zip"
            self.file_service.create_zip(pdf_files, zip_filename)

            self.ui.update_progress(progress_bar, status_text, 1.0, "Processamento concluído!")

            with open(zip_filename, "rb") as f:
                self.ui.download_button(
                    label="Baixar todos os PDFs (ZIP)",
                    data=f,
                    file_name=zip_filename,
                    mime="application/zip"
                )

            # Marcar para limpeza posterior
            st.session_state.cleanup_file = pdf_files + [zip_filename]
        else:
            self.ui.update_progress(progress_bar, status_text, 1.0, "Processamento concluído!")
            self.ui.show_warning("Nenhuma transcrição foi encontrada para os vídeos desta playlist.")