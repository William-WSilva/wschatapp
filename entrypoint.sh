#!/bin/bash

# Inicia o servidor Django
echo "Iniciando o servidor Django"
python manage.py runserver 0.0.0.0:8000 &

# Aguarda o servidor estar pronto
echo "Aguardando o servidor estar pronto..."
sleep 10

# Executa as migrações
echo "Executando as migrações"
python manage.py makemigrations
python manage.py migrate

# Coleta arquivos estáticos
echo "Coletando arquivos estáticos"
python manage.py collectstatic --no-input

# Mantém o contêiner em execução
echo "Contêiner em execução"
tail -f /dev/null
