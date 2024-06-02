# Weather API

Esta é uma aplicação FastAPI que fornece informações meteorológicas. A aplicação se conecta a uma API externa de clima e armazena os dados em um banco de dados MongoDB.


## Pré-requisitos

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Configuração

1. **Clone o repositório:**

    ```sh
    git clone https://github.com/seu-usuario/weather-api.git
    cd weather-api
    ```

2. **Crie um arquivo `.env` baseado no arquivo `env-example`:**

    ```sh
    cp env-example .env
    ```

3. **Atualize as variáveis de ambiente no arquivo `.env` conforme necessário.** 

## Como Rodar

1. **Construa e inicie os contêineres:**

    ```sh
    docker-compose up --build
    ```

2. **Acesse a aplicação:**

    Abra seu navegador e vá para `http://localhost:8000`.

3. **Documentação da API:**

    A documentação interativa da API estará disponível em `http://localhost:8000/docs`.

## Estrutura do Docker Compose

- **app**: Serviço que executa a aplicação FastAPI.
- **mongodb**: Serviço que executa o MongoDB.

## Comandos Úteis

- **Parar os contêineres:**

    ```sh
    docker-compose down
    ```

- **Ver logs dos contêineres:**

    ```sh
    docker-compose logs -f
    ```

- **Acessar o shell do contêiner da aplicação:**

    ```sh
    docker-compose exec app sh
    ```

## Observações

- Certifique-se de que as variáveis de ambiente no arquivo `.env` estejam corretas para a conexão com o MongoDB e a API externa.
- Se precisar mudar alguma configuração, atualize o `docker-compose.yaml` e o arquivo `.env`.
