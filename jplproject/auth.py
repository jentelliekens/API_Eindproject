from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from datetime import datetime, timedelta

import crud
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

SECRET_KEY = "5ce180b90f506982afa093546cf73bdb2abc07da6f6fc618c87efadcd7ecf477"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["argon2", "bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_access_token(data: dict):
    to_encode = data.copy()
    expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    # Adding the JWT expiration time case
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def authenticate_voetbalbond_user(db: Session, username: str, password: str):
    voetbalbond_user = crud.get_voetbalbond_user_by_email(db, username)
    if not voetbalbond_user:
        return False
    if not verify_password(password, voetbalbond_user.hashed_password):
        return False
    return voetbalbond_user


def get_current_voetbalbond_user(db: Session, token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    voetbalbond_user = crud.get_voetbalbond_user_by_email(db, username)
    if voetbalbond_user is None:
        raise credentials_exception
    return voetbalbond_user


def get_current_active_voetbalbond_user(db: Session, token: str = Depends(oauth2_scheme)):
    current_voetbalbond_user = get_current_voetbalbond_user(db, token)
    if not current_voetbalbond_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_voetbalbond_user
