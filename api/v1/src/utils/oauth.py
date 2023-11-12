from fastapi import Depends, HTTPException, status
from api.v1.src.utils.jwttoken import verify_token
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    Returns the current user based on the provided token.

    Args:
        token (str): The token to be verified.

    Raises:
        HTTPException: If the credentials cannot be validated.

    Returns:
        dict: The user information.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return verify_token(token, credentials_exception)
