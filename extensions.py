from passlib.context import CryptContext
from flask_jwt_extended import JWTManager

pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")
jwt = JWTManager()