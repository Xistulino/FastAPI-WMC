from fastapi import FastAPI, HTTPException
from typing import List
from models import User, Role
from uuid import UUID
 

app = FastAPI()

# Criação de dados para manipulação dos usuários.
db: List[User] = [
    User(
        id=UUID("12839e26-9cdd-421a-b2d8-398de2d9a499"),
        first_name="Ingrid", 
        last_name="Munhoz", 
        email="ingrid@ingrid.com", 
        role=[Role.role_1]
        ), 
        User(
        id=UUID("9da55b4c-4046-4c06-a3c9-d31df883c549"),
        first_name="Louisa", 
        last_name="Baldwin", 
        email="louisa@louisa.com", 
        role=[Role.role_2]            
        ),
        User(
        id=UUID("89f33ad3-62e4-46f6-805f-2b0d7573a87f"),
        first_name="Margaret", 
        last_name="Oliphant", 
        email="margaret@margaret.com", 
        role=[Role.role_2]            
        )


]

@app.get("/")
async def root():
    return {"message": "Olá, WoMakers!"}


######## CRIAÇÃO DE ROTAS HTTP ########

# Listagem de todos os usuários
@app.get("/api/users")
async def get_users():
    return db;


# Criar get para cada usuário 
@app.get("/api/users/{id}")
async def get_user(id: UUID):
    for user in db:
        if user.id == id:
            return user
    return {"message": "Usuário não encontrado!"}

#Criando novo usuário
@app.post("/api/users")
async def add_user(user: User):
    """
    Adiciona um usuário na base de dados.
    -**id**: UUID
    -**first_name**: str
    -**last_name**: str
    -**email**: str
    -**role**: Role
    """
    db.append(user)
    return {"Usuário criado com sucesso com o id: " : user.id}

#Deletar um usuário
@app.delete("/api/users/{id}")
async def remove_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return 
    raise HTTPException(
        status_code=404,
        detail=f'Usuario com id {id} não encontrado'
    )
