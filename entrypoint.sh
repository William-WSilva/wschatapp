#!/bin/bash

# Inicia o servidor Django
python manage.py runserver 0.0.0.0:8000 &

# Aguarda o servidor estar pronto
sleep 5

# Executa as migrações
python manage.py makemigrations
python manage.py migrate

# Mantém o contêiner em execução
tail -f /dev/null