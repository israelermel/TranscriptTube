import streamlit as st
from typing import Callable, Optional


class UIComponents:
    @staticmethod
    def header():
        """Renderiza o cabeçalho da aplicação."""
        st.title("Download de Transcrições do YouTube")
        st.write("Insira um link do YouTube para baixar a transcrição em PDF")

    @staticmethod
    def input_section() -> str:
        """Renderiza a seção de entrada da URL."""
        return st.text_input("URL do vídeo ou playlist do YouTube")

    @staticmethod
    def action_button(label: str = "Processar") -> bool:
        """Renderiza o botão de ação."""
        return st.button(label)

    @staticmethod
    def progress_indicator():
        """Renderiza indicadores de progresso."""
        progress = st.progress(0)
        status = st.empty()
        return progress, status

    @staticmethod
    def update_progress(progress_bar, status_text, value: float, message: str):
        """Atualiza o indicador de progresso."""
        progress_bar.progress(value)
        status_text.text(message)

    @staticmethod
    def show_success(message: str):
        """Mostra mensagem de sucesso."""
        st.success(message)

    @staticmethod
    def show_error(message: str):
        """Mostra mensagem de erro."""
        st.error(message)

    @staticmethod
    def show_warning(message: str):
        """Mostra mensagem de aviso."""
        st.warning(message)

    @staticmethod
    def show_info(message: str):
        """Mostra mensagem informativa."""
        st.info(message)

    @staticmethod
    def download_button(label: str, data, file_name: str, mime: str):
        """Renderiza um botão de download."""
        return st.download_button(
            label=label,
            data=data,
            file_name=file_name,
            mime=mime
        )

    @staticmethod
    def show_instructions():
        """Renderiza instruções de uso."""
        st.markdown("---")
        st.markdown("""
        ### Instruções:
        1. Cole o link de um vídeo do YouTube ou de uma playlist
        2. Clique em "Processar"
        3. Aguarde o processamento
        4. Baixe o arquivo PDF da transcrição ou o arquivo ZIP com todas as transcrições (no caso de playlist)

        **Observação:** O sistema só consegue extrair transcrições de vídeos que possuem legendas disponíveis.
        """)