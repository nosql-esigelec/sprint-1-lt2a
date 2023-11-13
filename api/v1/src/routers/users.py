"""
This module contains the routes for user management. It includes the following routes:
- POST /register: creates a new user
- POST /login: logs in a user
- GET /: retrieves a user by username
"""

from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm

from api.v1.src.dependencies import get_mongo_db
from api.v1.src.models.user import LoginResponse, SignUpResponse, UserLogged, UserSignUp
from api.v1.src.utils.jwttoken import create_access_token
from api.v1.src.utils.parsing import parse_mongo_id
from api.v1.src.services.users_service import UserService

router = APIRouter()

db = get_mongo_db()
user_service = UserService(db)


@router.post("/register", response_model=SignUpResponse)
def create_user(user: UserSignUp):
    """
    Create a new user.

    :param user: UserSignUp object containing user information.
    :type user: UserSignUp
    :return: Dictionary containing the user_id of the newly created user.
    :rtype: dict
    """
    user_object = dict(user)
    user_id = user_service.create_user(user_object).get("result")
    return {"user_id": user_id}


@router.post("/login", response_model=LoginResponse)
def login(request: OAuth2PasswordRequestForm = Depends()):
    """
    Login user.

    Authenticates the user with the provided username and password.
    If the user is authenticated, creates an access token and returns it along with the user details.

    Args:
        request (OAuth2PasswordRequestForm): The request object containing the username and password.

    Returns:
        dict: A dictionary containing the access token, token type and user details.
    """
    user = user_service.authenticate_user(request.username, request.password).get(
        "result"
    )

    user = parse_mongo_id(user, "user")
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No user found with this {request.username} username",
        )

    access_token = create_access_token(data={"sub": user["username"]})
    return {"access_token": access_token, "token_type": "bearer", "user": user}


@router.get("/", response_model=UserLogged)
def get_user(username: str):
    """
    Get user by username.

    Args:
        username (str): The username of the user to retrieve.

    Returns:
        dict: A dictionary containing the user's information, excluding their password.

    Raises:
        HTTPException: If no user is found with the given username.
    """
    current_user = user_service.get_user_by_username(
        username, projection={"password": 0}
    ).get("result")
    current_user = parse_mongo_id(current_user, "user")
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No user found with this {username} username",
        )
    return current_user
