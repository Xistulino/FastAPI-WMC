# FastAPI User Management API

Este projeto é uma API simples de gerenciamento de usuários construída com FastAPI. A API permite listar, adicionar, visualizar e remover usuários da base de dados simulada. Trata-se da minha primeira experiência com
FastAPI. O desenvolvimento é resultado das aulas do bootcamp em Python e Django ofertado pela WoMakersCode.

## Requisitos

Antes de começar, você precisará ter o seguinte instalado:

- Python 3.7 ou superior
- pip (gerenciador de pacotes do Python)
- FastAPI
- Uvicorn (servidor ASGI para rodar a aplicação)

## Instalação

Clone este repositório para sua máquina local:

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```

Navegue até o diretório do projeto:
 ```bash
   cd seu-repositorio
```

Crie e ative um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
.\venv\Scripts\activate   # Windows
```


Instale as dependências do projeto:
```bash
pip install -r requirements.txt
```


Para iniciar a aplicação, execute o seguinte comando:
```bash
uvicorn main:app --reload
