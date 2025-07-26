#!/bin/bash

echo "Inicializando aplicação Django..."

echo "Aguardando banco de dados estar disponível..."
while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
  sleep 1
done
echo "Banco de dados disponível!"

echo "PostgreSQL está no ar — iniciando comandos do Django..."

# Aplica migrações
echo "Aplicando migrações..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

# Coleta arquivos estáticos
echo "Coletando arquivos estáticos..."
python manage.py collectstatic --no-input

# Inicia o servidor
echo "Iniciando o servidor Django na porta 8000..."
python manage.py runserver 0.0.0.0:8000
