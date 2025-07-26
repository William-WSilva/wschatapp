# WsChatApp

### 📜 Descrição

Este é um aplicativo de postagem de imagens desenvolvido com HTML, CSS, Django, Docker e PostgreSQL. Possui mais de 10 telas e funcionalidades como:

- Login e cadastro
- Publicação de posts com imagens
- Alteração de dados cadastrais
- Busca de usuários
- Rede de seguidores
- Postagens salvas

---

<img src="./setup/static/assets/img/wschatapp4.png" width="600px" alt="Tela do WsChatApp">

## ⚛️ Tecnologias Utilizadas

- HTML + CSS
- Django
- Docker
- PostgreSQL
- Railway (para deploy)

---

## 🐳 Como executar localmente com Docker

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
```

## Acessar ambiente virtual

### 2. Acesse o ambiente virtual, senão crie e acesse
```bash
# criarambiente virtual
python -m venv venv

# acessar ambiente virtual
source venv/Scripts/activate
```


##  2. Criar variaveis ambiente .env

Crie um arquivo .env com o conteúdo:

```bash
# .env
DEBUG=1
SECRET_KEY=xxx
DJANGO_ALLOWED_HOSTS=xxx
DATABASE_ENGINE=django.db.backends.postgresql
DATABASE_NAME=xxx
DATABASE_USER=xxx
DATABASE_PASSWORD=xxx
DATABASE_HOST=db
DATABASE_PORT=5432
```

## 3. Subir os containers Docker

```bash
# !!! Somente Primeira vez ou quando mudar Dockerfile/dependências:
docker-compose up --build

# Para subir a aplicação (sem mudanças na imagem):
docker-compose up

# Para parar a aplicação:
docker-compose down

# Para parar e excluir volumes (zera o banco):
docker-compose down -v
```

Isso irá: 
- Subir o banco PostgreSQL local
- Aplicar migrações
- Coletar arquivos estáticos
- Rodar o servidor Django na porta 8010

### Acesse em: http://localhost:8010


## ATENÇÃO!!! Fazer Backup do Banco de Dados:


ATENÇÃO!!! -> Antes de parar a aplicação execute o backup do banco para não perder dados.
- Com a aplicação rodando acesse um terminal e rode:

```bash
# Criar backup do banco para restauração automática
docker exec -t container-wschatapp pg_dump -U wsilva -d wschatappdb > docker-entrypoint-initdb.d/initial_dump.sql

```


