from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.dependencies import get_db
from app.modules.auth.auth_schema import Register, Login
from app.modules.auth.auth_controller import registration, login

router = APIRouter(prefix = '/auth', tags = ['Authantication'])

@router.post('/signup', summary = 'Register an User')
def register(data: Register, db:Session = Depends(get_db)):
    return registration(db, data)

@router.post('/login', summary = 'Authanticate User')
def signin(data: Login, db: Session = Depends(get_db)):
    return login(db, data.email, data.password)