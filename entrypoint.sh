#!/bin/bash

echo "✅ Inicializando aplicação Django..."

echo "⏳ Aguardando banco de dados estar disponível..."
while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
  sleep 1
done
echo "✅ Banco de dados disponível!"

echo "🚀 PostgreSQL está no ar — iniciando comandos do Django..."

# Aplica migrações
echo "🔄 Aplicando migrações..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

# Restaura o dump inicial, se o arquivo existir
DUMP_FILE="docker-entrypoint-initdb.d/initial_dump.sql"
if [ -f "$DUMP_FILE" ]; then
  echo "📥 Importando dados de $DUMP_FILE..."
  PGPASSWORD=$DATABASE_PASSWORD psql -h $DATABASE_HOST -U $DATABASE_USER -d $DATABASE_NAME -f "$DUMP_FILE"
else
  echo "⚠️ Nenhum arquivo de dump encontrado em $DUMP_FILE. Pulando importação de dados."
fi

# Coleta arquivos estáticos
echo "📦 Coletando arquivos estáticos..."
python manage.py collectstatic --no-input

# Inicia o servidor com Gunicorn
echo "🌐 Iniciando o servidor Django na porta 8000 com Gunicorn..."
gunicorn setup.wsgi:application --bind 0.0.0.0:8000 --log-file -
