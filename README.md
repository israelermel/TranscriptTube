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

## 🚀 Instalação

### Pré-requisitos

- Python 3.7+
- pip (gerenciador de pacotes do Python)

### Passos para instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/TranscriptTube.git
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

## 🧠 Uso

1. Execute o aplicativo:

```bash
 python main.py
```

Isso iniciará o servidor Streamlit. O aplicativo será aberto automaticamente no seu navegador padrão, geralmente em http://localhost:8501.

2. Na interface do aplicativo:
   - Cole a URL do vídeo ou playlist do YouTube
   - Selecione os idiomas de preferência para as transcrições
   - Clique em "Processar"
   - Aguarde o processamento (a duração varia dependendo do número de vídeos)
   - Quando concluído, baixe os arquivos PDF ou o arquivo ZIP

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

## 💡 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests. Para grandes mudanças, por favor, abra primeiro um issue para discutir o que você gostaria de alterar.

### Possíveis melhorias

- Adicionar suporte para tradução automática das transcrições
- Melhorar o layout dos PDFs gerados
- Adicionar opção para exportar em outros formatos (TXT, Word, etc.)
- Implementar cache para melhorar a performance com playlists grandes
- Adicionar autenticação para permitir acesso a vídeos privados
- Implementar testes unitários e de integração

## 📝 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## 📧 Contato

Para dúvidas ou sugestões, entre em contato pelo [GitHub Issues](https://github.com/israelermel/TranscriptTube/issues) ou pelo email contato@israelermel.com.br.

---

Feito com ❤️ por [Israel Ermel](https://github.com/israelermel)
