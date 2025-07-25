# Use uma imagem base do Python
FROM python:3.11-slim  

# Define encoding e desativa bytecode .pyc
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Instala dependências do sistema necessárias (ex: para psycopg2)
RUN apt-get update && apt-get install -y \
    netcat-openbsd gcc postgresql-client libpq-dev \
    && apt-get clean

# Copia e instala dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código da aplicação
COPY . .

# Permissão para o entrypoint
RUN chmod +x entrypoint.sh

# Define o entrypoint
ENTRYPOINT ["./entrypoint.sh"]
