FROM python:3.12-slim

WORKDIR /app

# Copiar somente os arquivos necessários para instalar dependências primeiro
# Isso melhora o caching de camadas do Docker
COPY requirements.txt .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante dos arquivos do projeto
COPY . .

# Expor a porta que o Streamlit usará
EXPOSE 8501

# Definir variáveis de ambiente
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    STREAMLIT_SERVER_PORT=8501 \
    STREAMLIT_SERVER_HEADLESS=true \
    STREAMLIT_SERVER_ADDRESS=0.0.0.0

# Comando para iniciar a aplicação
CMD ["streamlit", "run", "run_app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.enableCORS=false", "--server.enableXsrfProtection=false"]

# Healthcheck para verificar se a aplicação está funcionando
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl --fail http://localhost:8501/ || exit 1
