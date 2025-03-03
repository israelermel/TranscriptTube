# web/ui_components.py
import streamlit as st
from typing import Callable, Optional, List, Tuple, Dict


class UIComponents:
    # Lista de idiomas comuns com seus códigos
    COMMON_LANGUAGES = {
        'Português': 'pt',
        'Inglês': 'en',
        'Espanhol': 'es',
        'Francês': 'fr',
        'Alemão': 'de',
        'Italiano': 'it',
        'Japonês': 'ja',
        'Chinês': 'zh',
        'Russo': 'ru',
        'Árabe': 'ar',
        'Hindi': 'hi',
        'Coreano': 'ko'
    }

    @staticmethod
    def header():
        """Renderiza o cabeçalho da aplicação."""
        st.title("TranscriptTube")
        st.write("Insira um link do YouTube para baixar a transcrição em PDF")

    @staticmethod
    def input_section() -> str:
        """Renderiza a seção de entrada da URL."""
        return st.text_input("URL do vídeo ou playlist do YouTube")

    @staticmethod
    def language_selector() -> List[str]:
        """Renderiza o seletor de idiomas para transcrições.

        Returns:
            Lista de códigos de idioma selecionados pelo usuário
        """
        st.subheader("Preferências de Idioma")
        st.write("Selecione os idiomas que você deseja para as transcrições (em ordem de preferência):")

        # Criar três colunas para os seletores de idioma
        col1, col2, col3 = st.columns(3)

        # Primeira preferência (obrigatória)
        with col1:
            primary_lang = st.selectbox(
                "Idioma primário (obrigatório)",
                options=list(UIComponents.COMMON_LANGUAGES.keys()),
                index=0,  # Português como padrão
                key="primary_lang"
            )

        # Segunda preferência (opcional)
        with col2:
            secondary_options = ["Nenhum"] + list(UIComponents.COMMON_LANGUAGES.keys())
            secondary_lang = st.selectbox(
                "Idioma secundário (opcional)",
                options=secondary_options,
                index=1,  # Inglês como padrão na posição 1
                key="secondary_lang"
            )

        # Terceira preferência (opcional)
        with col3:
            tertiary_options = ["Nenhum"] + list(UIComponents.COMMON_LANGUAGES.keys())
            tertiary_lang = st.selectbox(
                "Idioma terciário (opcional)",
                options=tertiary_options,
                index=0,  # Nenhum como padrão
                key="tertiary_lang"
            )

        # Opção para tentar todos os idiomas disponíveis se os selecionados não estiverem disponíveis
        fallback_option = st.checkbox(
            "Tentar outros idiomas se os selecionados não estiverem disponíveis",
            value=True,
            key="fallback_option"
        )

        # Converter as seleções em códigos de idioma
        selected_langs = []

        # Adicionar idioma primário (obrigatório)
        selected_langs.append(UIComponents.COMMON_LANGUAGES[primary_lang])

        # Adicionar idioma secundário (se selecionado)
        if secondary_lang != "Nenhum":
            selected_langs.append(UIComponents.COMMON_LANGUAGES[secondary_lang])

        # Adicionar idioma terciário (se selecionado)
        if tertiary_lang != "Nenhum":
            selected_langs.append(UIComponents.COMMON_LANGUAGES[tertiary_lang])

        # Se a opção de fallback estiver marcada e nenhum idioma secundário/terciário foi selecionado,
        # adicionar mais alguns idiomas comuns
        if fallback_option and len(selected_langs) < 3:
            # Adicionar qualquer idioma comum que ainda não esteja na lista
            for lang_code in UIComponents.COMMON_LANGUAGES.values():
                if lang_code not in selected_langs:
                    selected_langs.append(lang_code)
                    # Limitar a 5 idiomas no total para não sobrecarregar
                    if len(selected_langs) >= 5:
                        break

        return selected_langs

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
    def download_button(label: str, data, file_name: str, mime: str, key: str = None):
        """Renderiza um botão de download.

        Args:
            label: Texto do botão
            data: Dados a serem baixados
            file_name: Nome do arquivo para download
            mime: Tipo MIME do arquivo
            key: Identificador único para o botão (opcional)
        """
        return st.download_button(
            label=label,
            data=data,
            file_name=file_name,
            mime=mime,
            key=key
        )

    @staticmethod
    def show_instructions():
        """Renderiza instruções de uso."""
        st.markdown("---")
        st.markdown("""
        ### Instruções:
        1. Cole o link de um vídeo do YouTube ou de uma playlist
        2. Selecione os idiomas desejados para as transcrições
        3. Clique em "Processar"
        4. Aguarde o processamento
        5. Baixe o arquivo PDF da transcrição ou o arquivo ZIP com todas as transcrições (no caso de playlist)

        **Observação:** O sistema só consegue extrair transcrições de vídeos que possuem legendas disponíveis nos idiomas selecionados.
        Se nenhuma legenda estiver disponível nos idiomas escolhidos, o sistema tentará encontrar transcrições em outros idiomas,
        caso a opção "Tentar outros idiomas" esteja marcada.
        """)

    @staticmethod
    def show_available_languages(available_transcripts: List[Dict]):
        """Mostra informações sobre as transcrições disponíveis para um vídeo.

        Args:
            available_transcripts: Lista de dicionários com informações das transcrições
        """
        if not available_transcripts:
            st.warning("Não foi possível recuperar informações sobre as transcrições disponíveis.")
            return

        st.write("### Transcrições disponíveis para este vídeo:")

        # Criar tabela de transcrições disponíveis
        transcript_data = []
        for transcript in available_transcripts:
            transcript_data.append({
                "Idioma": transcript['language'],
                "Código": transcript['language_code'],
                "Gerada automaticamente": "Sim" if transcript['is_generated'] else "Não",
                "Traduzível": "Sim" if transcript['is_translatable'] else "Não"
            })

        st.table(transcript_data)

    # Adicione isso na classe UIComponents em web/ui_components.py
    @staticmethod
    def keep_files_option():
        """Renderiza a opção para manter os arquivos após o download."""
        return st.checkbox("Manter arquivos na pasta downloads após o download", value=False, key="keep_files")