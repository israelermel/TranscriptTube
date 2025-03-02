# main.py
import os
import sys
import subprocess


def is_streamlit_context():
    """Verifica se o código está sendo executado no contexto do Streamlit."""
    return 'streamlit.runtime.scriptrunner.script_runner' in sys.modules


def main():
    """Ponto de entrada principal que garante que a aplicação seja
    iniciada corretamente com o Streamlit."""

    # Se já estivermos no contexto do Streamlit ou se o arquivo foi chamado com 'streamlit run'
    if is_streamlit_context() or any('streamlit' in arg for arg in sys.argv):
        # Apenas importe e execute a aplicação
        try:
            from web.app import StreamlitApp
            app = StreamlitApp()
            app.run()
        except ImportError:
            import streamlit as st
            st.error("Erro de importação. Verifique se a estrutura do projeto está correta.")
            st.info("Certifique-se de executar este arquivo a partir da raiz do projeto:")
            st.code("streamlit run main.py")
    else:
        # Estamos sendo executados diretamente pelo Python, então iniciamos o streamlit
        # como um processo separado *uma única vez*
        file_path = os.path.abspath(__file__)
        print(f"Iniciando o Streamlit para: {file_path}")

        try:
            # Garantimos que estamos na pasta correta para importações relativas
            project_dir = os.path.dirname(file_path)
            os.chdir(project_dir)

            # Executamos o streamlit como um processo separado e esperamos que termine
            subprocess.run(["streamlit", "run", file_path], check=True)
        except FileNotFoundError:
            print("Erro: streamlit não foi encontrado. Certifique-se de que ele está instalado.")
            print("Você pode instalá-lo com: pip install streamlit")
        except subprocess.CalledProcessError as e:
            print(f"Erro ao iniciar o Streamlit: {e}")


if __name__ == "__main__":
    main()