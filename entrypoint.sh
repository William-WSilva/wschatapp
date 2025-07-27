#!/bin/bash

echo "🚀 Inicializando aplicação Django..."

echo "⏳ Aguardando banco de dados estar disponível..."
while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
  sleep 1
done
echo "✅ Banco de dados disponível!"

echo "⚙️ Aplicando migrações do Django..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

# Verifica e restaura o dump somente se o banco estiver vazio
DUMP_FILE="docker-entrypoint-initdb.d/initial_dump.sql"
if [ -f "$DUMP_FILE" ]; then
  echo "🔍 Verificando se o banco está vazio para importar dados..."
  USER_COUNT=$(PGPASSWORD=$DATABASE_PASSWORD psql -h $DATABASE_HOST -U $DATABASE_USER -d $DATABASE_NAME -tAc "SELECT COUNT(*) FROM auth_user;")

  if [ "$USER_COUNT" -eq "0" ]; then
    echo "📥 Importando dados de $DUMP_FILE..."
    PGPASSWORD=$DATABASE_PASSWORD psql -h $DATABASE_HOST -U $DATABASE_USER -d $DATABASE_NAME -f "$DUMP_FILE"
  else
    echo "ℹ️ Banco já possui dados. Importação ignorada."
  fi
else
  echo "⚠️ Arquivo de dump $DUMP_FILE não encontrado. Pulando importação."
fi

echo "📦 Coletando arquivos estáticos..."
python manage.py collectstatic --no-input

echo "🌐 Iniciando o servidor Django na porta 8000 com Gunicorn..."
gunicorn setup.wsgi:application --bind 0.0.0.0:8000 --log-file -
