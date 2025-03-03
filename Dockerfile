FROM python:3.9-slim

WORKDIR /app

# Copiar os arquivos necessários
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante dos arquivos do projeto
COPY . .

# Criar diretório para downloads
RUN mkdir -p /app/downloads && chmod 777 /app/downloads

# Criar arquivo de configuração do Streamlit
RUN mkdir -p /app/.streamlit
RUN echo '[server]\nenableCORS = false\nenableXsrfProtection = false\n\n[browser]\ngatherUsageStats = false\n\n[theme]\nbase = "dark"' > /app/.streamlit/config.toml

# Expor a porta
EXPOSE 8501

# Configurar variáveis de ambiente
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    STREAMLIT_SERVER_PORT=8501 \
    STREAMLIT_SERVER_ADDRESS=0.0.0.0

# Comando para iniciar a aplicação
CMD ["streamlit", "run", "run_app.py", "--server.port=8501", "--server.address=0.0.0.0"]