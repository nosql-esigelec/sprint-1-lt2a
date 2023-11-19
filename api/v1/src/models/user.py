"""
This module contains Pydantic models for user authentication and authorization.

Models:
- UserSignUp: Model for user sign up request.
- UserLogged: Model for logged in user.
- SignUpResponse: Model for sign up response.
- LoginResponse: Model for login response.
- Login: Model for user login request.
- Token: Model for token response.
- TokenData: Model for token data.
"""
from typing import Optional, Dict

from pydantic import BaseModel, validator


class UserSignUp(BaseModel):
    """
    Represents a user sign up request.

    Attributes:
        username (str): The username of the user.
        email (str): The email address of the user.
        password (str): The password of the user.
    """

    username: str
    email: str
    password: str


class UserLogged(BaseModel):
    """
    UserLogged model for logged in user.

    Attributes:
    -----------
    uid : str
        The unique identifier of the user.
    org_id : str
        The unique identifier of the organization the user belongs to.
    username : str
        The username of the user.
    email : str
        The email address of the user.
    """

    uid: str
    org_id: str
    username: str
    email: str
    
    @validator('org_id', pre=True)
    def extract_result_from_org_id(cls, v):
        if isinstance(v, Dict) and 'result' in v:
            return str(v['result'])  # Convert ObjectId in str if necessary
        return v


class SignUpResponse(BaseModel):
    """
    Model for sign up response.

    Attributes:
    ----------
    user_id : str
        The ID of the user who signed up.
    """

    user_id: str


class LoginResponse(BaseModel):
    """
    Represents a response to a login request.

    Attributes:
        access_token (str): The access token for the user.
        token_type (str): The type of token.
        user (UserLogged): The logged in user.
    """

    access_token: str
    token_type: str
    user: UserLogged


class Login(BaseModel):
    """
    Login model for user login request.

    Attributes:
    ----------
    username : str
        The username of the user.
    password : str
        The password of the user.
    """

    username: str
    password: str


class Token(BaseModel):
    """
    Token model for token response.

    Attributes:
    -----------
    access_token : str
        The access token generated for the user.
    token_type : str
        The type of token generated.
    """

    access_token: str
    token_type: str


class TokenData(BaseModel):
    """
    TokenData model for token data.

    Attributes:
        username (Optional[str]): The username associated with the token.
    """

    username: Optional[str] = None
