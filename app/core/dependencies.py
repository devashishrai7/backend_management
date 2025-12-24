from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.config import settings
from app.modules.auth.auth_model import User

oauth2 = OAuth2PasswordBearer(tokenUrl = "/auth/login")

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()
    
def get_current_user(token: str = Depends(oauth2), db:Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms = [settings.ALGORITHM])
        email = payload.get("sub")
    except JWTError:
        raise HTTPException(status_code= 401, detail= "Invalid token")
    
    user  = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code= 401, detail= "Unauthenticated")
    return user