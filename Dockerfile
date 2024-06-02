# Use uma imagem base oficial do Python Alpine
FROM python:3.8-alpine

#Dependências necessárias do sistema para compilar algumas libs do python
RUN apk update && apk add --no-cache gcc musl-dev libffi-dev
WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app /app/app
COPY main.py .
COPY .env .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
