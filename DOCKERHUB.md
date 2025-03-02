# Publicando TranscriptTube no Docker Hub

Este guia explica como publicar sua imagem TranscriptTube no Docker Hub para compartilhá-la com outros usuários.

## Pré-requisitos

1. Crie uma conta no [Docker Hub](https://hub.docker.com/).
2. Instale o Docker em sua máquina local.
3. Faça login no Docker Hub a partir do terminal:

```bash
docker login
```

## Passos para publicação

### 1. Construa a imagem Docker localmente

```bash
# Na pasta raiz do projeto
docker build -t transcript-tube .
```

### 2. Marque (tag) a imagem com seu nome de usuário do Docker Hub

```bash
docker tag transcript-tube israelermel/transcript-tube:latest
```

Você também pode adicionar uma tag de versão específica:

```bash
docker tag transcript-tube israelermel/transcript-tube:1.0.0
```

### 3. Envie a imagem para o Docker Hub

```bash
# Enviar a versão "latest"
docker push israelermel/transcript-tube:latest

# Enviar uma versão específica (se aplicável)
docker push israelermel/transcript-tube:1.0.0
```

### 4. Verifique sua imagem no Docker Hub

Visite `https://hub.docker.com/r/israelermel/transcript-tube` para confirmar que sua imagem foi publicada corretamente.

## Atualizando sua imagem

Para atualizar sua imagem quando fizer alterações no código:

1. Construa novamente a imagem local:
```bash
docker build -t transcript-tube .
```

2. Marque com a mesma tag (ou crie uma nova versão):
```bash
docker tag transcript-tube israelermel/transcript-tube:latest
docker tag transcript-tube israelermel/transcript-tube:1.0.1
```

3. Envie as novas versões:
```bash
docker push israelermel/transcript-tube:latest
docker push israelermel/transcript-tube:1.0.1
```

## Melhorando sua publicação no Docker Hub

Para tornar sua imagem mais útil e profissional no Docker Hub:

1. Adicione uma descrição detalhada no repositório do Docker Hub
2. Inclua exemplos de uso
3. Especifique requisitos de hardware
4. Documente as variáveis de ambiente disponíveis
5. Liste os volumes que podem ser montados

## Automatizando com GitHub Actions

Você pode configurar o GitHub Actions para construir e publicar automaticamente sua imagem Docker quando ocorrerem mudanças no repositório:

1. Crie um arquivo `.github/workflows/docker-publish.yml` com o seguinte conteúdo:

```yaml
name: Docker

on:
  push:
    branches: [ main ]
    tags: [ 'v*.*.*' ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Login to DockerHub
        uses: docker/login-action@v1
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}
          
      - name: Build and push
        uses: docker/build-push-action@v2
        with:
          context: .
          push: true
          tags: ${{ secrets.DOCKERHUB_USERNAME }}/transcript-tube:latest
```

2. Configure os secrets `DOCKERHUB_USERNAME` e `DOCKERHUB_TOKEN` nas configurações do seu repositório GitHub.

Este processo automatizará a publicação da sua imagem Docker toda vez que você fizer um push para a branch principal ou criar uma nova tag.
