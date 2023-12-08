#!/bin/bash

# Inicia o servidor Django
echo "Iniciando o servidor Django"
python manage.py runserver 0.0.0.0:8000 &

# Aguarda o servidor estar pronto
echo "Aguardando o servidor estar pronto..."
sleep 30

# Executa as migrações
echo "Executando as migrações"
python manage.py makemigrations
python manage.py migrate

# Mantém o contêiner em execução
echo "Contêiner em execução"
tail -f /dev/null
