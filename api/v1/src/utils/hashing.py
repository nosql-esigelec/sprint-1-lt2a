from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash:
    """
    A utility class for hashing and verifying passwords using bcrypt algorithm.
    """
    def bcrypt(password: str):
        return pwd_cxt.hash(password)

    def verify(hashed, normal):
        return pwd_cxt.verify(normal, hashed)
