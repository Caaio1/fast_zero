from pydantic import BaseModel
from pydantic.networks import EmailStr

class Message(BaseModel):
    message: str

class UserPublic(BaseModel):
     id: int 
     username: str
     email: str
   

class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str               

class UserDB(UserSchema):
    id: int

    
class UserList(BaseModel):
    users: list[UserPublic]