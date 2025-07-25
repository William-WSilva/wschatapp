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
# Iniciar aplicação
docker-compose up --build

# Parar aplicação
docker-compose down
```

Isso irá: 
- Subir o banco PostgreSQL local
- Aplicar migrações
- Coletar arquivos estáticos
- Rodar o servidor Django na porta 8010

### Acesse em: http://localhost:8010


## ATENÇÃO!!! Fazer Backup do Banco de Dados:

Fazer um backup do banco de dados e desligar aplicação, será executado comandos do arquivo 
``Makefile``

ATENÇÃO!!! -> Antes de parar a aplicação execute o backup do banco para não perder dados.
- Com a aplicação rodando acesse um terminal e rode:

```bash
# comando para gerar o backup na pasta: backups/
1. docker exec -t container-wschatapp pg_dump -U wsilva -d wschatappdb > backups/initial_dump.sql

# comando para copiar o backup para a pasta: docker-entrypoint-initdb.d/
2. cp backups/initial_dump.sql docker-entrypoint-initdb.d/initial_dump.sql
```


