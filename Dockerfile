# Use uma imagem base do Python
FROM python:3.8

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie o requirements.txt para o contêiner e instale as dependências
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copie o código do projeto para o contêiner
COPY . /app/

# Copie o entrypoint.sh para o contêiner
COPY entrypoint.sh /app/entrypoint.sh

# Defina permissões de execução para o entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Comando para iniciar o servidor usando o entrypoint
CMD ["./entrypoint.sh"]