from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta, timezone
from app.config import settings

pwd = CryptContext(schemes = ['bcrypt'], deprecated = 'auto')

def hash_password(password):
    return pwd.hash(password)

def verify_password(password, hashed_password):
    return pwd.verify(password, hashed_password)

def create_token(data: dict):
    expire = datetime.now(timezone.utc) + timedelta(minutes= settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    data.update({'exp' : expire})
    access_token = jwt.encode(data, settings.JWT_SECRET_KEY, algorithm = settings.ALGORITHM)
    return access_token