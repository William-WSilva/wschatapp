#!/bin/bash

echo "Inicializando aplicação Django..."

# Aplica migrações
echo "Aplicando migrações..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

# Coleta arquivos estáticos
echo "Coletando arquivos estáticos..."
python manage.py collectstatic --no-input

# Backup do banco local Postgres (dentro do container)
echo "Criando backup do banco de dados..."
pg_dump -U postgres -d postgres > /app/backups/backup_$(date +%Y%m%d_%H%M%S).sql

# Inicia o servidor
echo "Iniciando o servidor Django na porta 8000..."
python manage.py runserver 0.0.0.0:8000
