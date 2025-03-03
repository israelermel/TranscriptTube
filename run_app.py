#!/usr/bin/env python
"""
Script de inicialização para o TranscriptTube.
Este arquivo deve estar na raiz do projeto e é usado pelo Streamlit para iniciar o aplicativo.
"""
import os
import sys
import streamlit as st

# Configurações para remover elementos de UI indesejados
st.set_page_config(
    page_title="TranscriptTube",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': "# TranscriptTube\nBaixe transcrições de vídeos do YouTube em PDF."
    }
)

# CSS muito mais específico para esconder elementos de UI do Streamlit incluindo deploy e outros
hide_streamlit_style = """
<style>
/* Esconder botões de deploy em todas as versões/seletores possíveis do Streamlit */
.stDeployButton, [data-testid="stDeployButton"], button[title="Deploy"], 
div[class*="stDeployButton"], div[class*="deployButton"], 
button[data-testid="deploy"], .streamlit-button.primary,
[data-baseweb="button"][kind="primary"],
button[kind="primary"], 
div:has(> [data-testid="stToolbar"]) button,
.overlayBtn, .css-demzbm, .css-54f03e {
    display: none !important;
    visibility: hidden !important;
    width: 0 !important;
    height: 0 !important;
    padding: 0 !important;
    margin: 0 !important;
    border: none !important;
    position: absolute !important;
    overflow: hidden !important;
    clip: rect(0 0 0 0) !important;
}

/* Esconder menu e barra superior, adequando para várias versões */
#MainMenu, [data-testid="MainMenu"], .stApp > header,
.main-menu, div[data-testid="stHeader"],
.css-14xtw13, .css-18ni7ap, .css-qj8ax5, .css-1aehpvj, .css-y1rsc7 {
    display: none !important;
    visibility: hidden !important;
}

/* Esconder rodapé em todas as versões */
footer, .footer, div[data-testid="stFooter"], 
.css-1lsmgbg, .css-1p3t4dp, .reportview-container footer,
.css-qri22k, .css-17ziqus, .css-1b0udgb, .css-qq0ne6 {
    display: none !important;
    visibility: hidden !important;
}

/* Remover barra lateral e elementos de navegação */
[data-testid="collapsedControl"], 
div.streamlit-expanderHeader, .sidebar .sidebar-collapse-control,
.sidebar-content, .sidebar-close-button,
.css-1d391kg, .css-12oz5g7, [data-testid="collapsedControl"],
.css-14xtw13, [data-testid="collapsedControl"] {
    display: none !important;
    visibility: hidden !important;
}

/* Ajustar margens e padding da página principal */
.stApp {
    max-width: 100% !important;
}

.css-18e3th9, .css-1d391kg, .css-1lsmgbg,
.stApp > div:first-child > div:first-child,
.appview-container .main .block-container {
    padding-top: 1rem !important;
    padding-right: 1rem !important;
    padding-left: 1rem !important;
    padding-bottom: 10rem !important;
}

/* Esconder barra de ferramentas lateral */
div[data-testid="stToolbar"], div[class*="Toolbar"],
.stToolbar, div[class*="stToolbar"] {
    display: none !important;
    visibility: hidden !important;
}

/* Esconder elementos decorativos */
div[data-testid="stDecoration"], div[class*="stDecoration"],
div[class*="decoration"], .decoration, .stDecoration,
div.decorationContent {
    display: none !important;
    visibility: hidden !important;
}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Adiciona o diretório raiz ao sys.path para permitir importações
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

try:
    # Tenta importar a aplicação
    from web.app import StreamlitApp

    # Executa a aplicação
    app = StreamlitApp()
    app.run()
except ImportError as e:
    st.error(f"Erro ao importar a aplicação: {e}")
    st.info("Verificando estrutura do projeto...")

    # Verifica quais diretórios existem
    expected_dirs = ['api', 'web', 'models', 'utils']
    for d in expected_dirs:
        path = os.path.join(current_dir, d)
        if os.path.isdir(path):
            st.success(f"✓ Diretório {d} encontrado")
            files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
            st.code(f"Arquivos em {d}/: {', '.join(files)}")
        else:
            st.error(f"✗ Diretório {d} não encontrado")

    st.error("Não foi possível iniciar o aplicativo. Verifique a estrutura do projeto.")