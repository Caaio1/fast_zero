from fastapi.responses import HTMLResponse
from http import HTTPStatus
from fastapi import FastAPI, HTTPException
from fast_zero1.schemas import UserSchema, UserPublic, UserDB, UserList

database = []

app = FastAPI()


@app.get('/', response_class=HTMLResponse)
def read_root():
    return """
    <html>
      <head>
        <title> Nosso olá mundo!</title>
      </head>
      <body>
        <h1>ola mundo</h1>
      </body>
    </html>"""



@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    id = len(database) + 1
    # Cria uma instância real com os dados do usuário
    user_with_id = UserDB(**user.dict(), id=id)
    database.append(user_with_id)
    return UserPublic(username=user_with_id.username, email=user_with_id.email, id=user_with_id.id)

@app.get('/users/', response_model=UserList)
def read_users():
    return {'users': database}

@app.put('/users/{user_id}', response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=user_id)
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )
    database[user_id - 1] = user_with_id

    return user_with_id
@app.delete('/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic)
def delete_user(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )
    user = database.pop(user_id - 1)
    return user