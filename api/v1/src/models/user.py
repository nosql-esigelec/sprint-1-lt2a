from pydantic import BaseModel
from typing import Optional


class UserSignUp(BaseModel):
    username: str
    email: str
    password: str

class UserLogged(BaseModel):
    uid: str
    org_id: str
    username: str
    email: str
    

class SignUpResponse(BaseModel):
    user_id: str

class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    user: UserLogged
class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
