"""
User routes.
"""
from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm

from src.dependencies import get_mongo_db
from src.models.user import LoginResponse, SignUpResponse, UserLogged, UserSignUp
from src.utils.jwttoken import create_access_token
from src.utils.parsing import parse_mongo_id
from src.services.users_service import UserService

router = APIRouter()

db = get_mongo_db()
user_service = UserService(db)


@router.post("/register", response_model=SignUpResponse)
def create_user(user: UserSignUp):
    """
    Create a new user.
    """
    user_object = dict(user)
    user_id = user_service.create_user(user_object).get("result")
    return {"user_id": user_id}


@router.post("/login", response_model=LoginResponse)
def login(request: OAuth2PasswordRequestForm = Depends()):
    """
    Login user.
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
