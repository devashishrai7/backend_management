from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.modules.auth.auth_model import User
from app.modules.auth.auth_schema import Register
from app.core.security import hash_password, verify_password, create_token


def registration(db:Session, data: Register):
    if db.query(User).filter(User.email == data.email).first():
        raise HTTPException(status_code = 400, detail = "User exists")
    user = User(
        name = data.name,
        email = data.email,
        phone_number = data.phone_number,
        password = hash_password(data.password)
    )
    db.add(user)
    db.commit()
    return {
        'success' : True,
        'message' : 'User created successfully'
    }

def login(db: Session, email: str, password: str):
    print(email, password)
    user = db.query(User).filter(User.email == email).first()
    print(user)
    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code = 401, detail = {
            'success': False,
            'message': 'Invalid credentials'
            }
        )
    token = create_token({
        'sub' : user.email,
    })
    return {
        'success' : True,
        'message' : 'Logged-in successfully',
        'access_token' : token,
        'token_type' : 'bearer'
    }