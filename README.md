# TranscriptTube

Um aplicativo web para download de transcrições de vídeos do YouTube em formato PDF.

![Banner TranscriptTube](https://via.placeholder.com/1200x300.png?text=TranscriptTube)

## 📋 Descrição

TranscriptTube é um aplicativo construído com Streamlit que permite aos usuários baixar as transcrições/legendas de vídeos do YouTube em formato PDF. O aplicativo suporta tanto vídeos individuais quanto playlists completas, e permite que o usuário selecione os idiomas de preferência para as transcrições.

### ✨ Funcionalidades

- 📹 Processamento de vídeos individuais ou playlists completas
- 🌐 Seleção de múltiplos idiomas para transcrições em ordem de preferência
- 📊 Visualização de idiomas disponíveis para cada vídeo
- 📄 Exportação das transcrições para arquivos PDF
- 📦 Compactação de múltiplas transcrições em um único arquivo ZIP
- 🔄 Interface simples e intuitiva com feedback em tempo real
- 🐳 Disponível como imagem Docker para fácil implantação

## 🚀 Instalação e Uso

Você pode executar o TranscriptTube de três maneiras diferentes:

### Método 1: Usando Docker (Recomendado) 🐳

A maneira mais fácil de executar o TranscriptTube é usando Docker:

```bash
docker run -p 8501:8501 israelermel/transcript-tube:latest
```

Acesse http://localhost:8501 no seu navegador.

### Método 2: Usando Docker Compose 🐙

1. Clone o repositório:

```bash
git clone https://github.com/israelermel/TranscriptTube.git
cd TranscriptTube
```

2. Inicie a aplicação com Docker Compose:

```bash
docker-compose up -d
```

3. Acesse http://localhost:8501 no seu navegador.

Para parar a aplicação:

```bash
docker-compose down
```

### Método 3: Instalação Local (Python) 🐍

#### Pré-requisitos

- Python 3.7+
- pip (gerenciador de pacotes do Python)

#### Passos para instalação

1. Clone o repositório:

```bash
git clone https://github.com/israelermel/TranscriptTube.git
cd TranscriptTube
```

2. Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv

# No Windows
venv\Scripts\activate

# No macOS/Linux
source venv/bin/activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute o aplicativo:

```bash
python run_app.py
```

## 📱 Como Usar

1. Acesse a interface da aplicação no navegador (geralmente em http://localhost:8501)
2. Cole a URL do vídeo ou playlist do YouTube
3. Selecione os idiomas de preferência para as transcrições
4. Clique em "Processar"
5. Aguarde o processamento (a duração varia dependendo do número de vídeos)
6. Quando concluído, baixe os arquivos PDF ou o arquivo ZIP

## 🐳 Criando sua própria imagem Docker

Se você deseja construir a imagem Docker localmente:

```bash
# Construir a imagem
docker build -t transcript-tube .

# Executar o container
docker run -p 8501:8501 transcript-tube
```

## 🧩 Estrutura do Projeto

O projeto segue princípios SOLID e está organizado da seguinte forma:

```
TranscriptTube/
├── api/                  # Lógica de negócios e serviços
│   ├── __init__.py
│   ├── youtube_service.py    # Serviço para interação com o YouTube
│   ├── transcript_service.py # Serviço para gerenciamento de transcrições
│   ├── pdf_service.py        # Serviço para geração de PDFs
│   └── file_service.py       # Serviço para gerenciamento de arquivos
├── web/                  # Interface do usuário (Streamlit)
│   ├── __init__.py
│   ├── app.py                # Aplicação principal
│   └── ui_components.py      # Componentes da interface do usuário
├── models/               # Modelos de dados
│   ├── __init__.py
│   └── data_models.py        # Classes de modelo de dados
├── utils/                # Utilitários
│   ├── __init__.py
│   └── url_utils.py          # Funções para manipulação de URLs
├── Dockerfile            # Configuração para build da imagem Docker
├── docker-compose.yml    # Configuração para execução com Docker Compose
├── run_app.py            # Script para execução da aplicação
├── requirements.txt      # Dependências do projeto
└── README.md             # Este arquivo
```

## 📦 Dependências

As principais dependências do projeto são:

- `streamlit`: Para a interface web
- `pytube`: Para interação com a API do YouTube
- `youtube-transcript-api`: Para extração de transcrições de vídeos
- `fpdf`: Para geração de arquivos PDF

Veja o arquivo `requirements.txt` para a lista completa de dependências.

## 🔧 Configurações Avançadas com Docker

O TranscriptTube pode ser configurado com variáveis de ambiente quando executado com Docker:

```bash
docker run -p 8501:8501 \
  -e STREAMLIT_THEME="dark" \
  -v $(pwd)/downloads:/app/downloads \
  israelermel/transcript-tube:latest
```

### Opções de configuração:

- `-p 8501:8501`: Mapeia a porta 8501 do container para a porta 8501 do host
- `-v $(pwd)/downloads:/app/downloads`: Monta um volume para salvar os arquivos baixados localmente
- `-e STREAMLIT_THEME="dark"`: Define o tema do Streamlit (opcional)

## 💡 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests. Para grandes mudanças, por favor, abra primeiro um issue para discutir o que você gostaria de alterar.

### Possíveis melhorias

- Adicionar suporte para tradução automática das transcrições
- Melhorar o layout dos PDFs gerados
- Adicionar opção para exportar em outros formatos (TXT, Word, etc.)
- Implementar cache para melhorar a performance com playlists grandes
- Adicionar autenticação para permitir acesso a vídeos privados
- Implementar testes unitários e de integração
- Criar pipeline de CI/CD para construção e publicação automática da imagem Docker

## 📝 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## 📧 Contato

Para dúvidas ou sugestões, entre em contato pelo [GitHub Issues](https://github.com/israelermel/TranscriptTube/issues) ou pelo email seuemail@exemplo.com.

---

Feito com ❤️ por [Seu Nome](https://github.com/israelermel)
