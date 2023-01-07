from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
# from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

import auth
import crud
import models
import schemas
from database import SessionLocal, engine
import os

if not os.path.exists('sqlitedb'):
    os.makedirs('sqlitedb')

#"sqlite:///./sqlitedb/sqlitedata.db"
models.Base.metadata.create_all(bind=engine)

jplApp = FastAPI()


# origins = [
#     "http://localhost",
#     "http://localhost:8080",
#     "https://localhost.tiangolo.com",
#     "http://127.0.0.1:5500"
#     "https://useritem-api-service-api-eindproject-jentelliekens.cloud.okteto.net/"
# ]

# jplApp.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@jplApp.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    voetbalbond_user = auth.authenticate_voetbalbond_user(db, form_data.username, form_data.password)
    if not voetbalbond_user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = auth.create_access_token(
        data={"sub": voetbalbond_user.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}


@jplApp.post("/users/", response_model=schemas.User)
def create_voetbalbond_user(voetbalbond_user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_jpl = crud.get_voetbalbond_user_by_email(db, email=voetbalbond_user.email)
    if db_jpl:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_voetbalbond_user(db=db, voetbalbond_user=voetbalbond_user)


@jplApp.get("/users/", response_model=list[schemas.User])
def read_voetbalbond_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    voetbalbond_users = crud.get_voetbalbond_users(db, skip=skip, limit=limit)
    return voetbalbond_users


@jplApp.get("/users/me", response_model=schemas.User)
def read_voetbalbond_users_me(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    current_voetbalbond_user = auth.get_current_active_voetbalbond_user(db, token)
    return current_voetbalbond_user


@jplApp.get("/users/{voetbalbond_user_id}", response_model=schemas.User)
def read_voetbalbond_user(voetbalbond_user_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_jpl = crud.get_voetbalbond_user(db, voetbalbond_user_id=voetbalbond_user_id)
    if db_jpl is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_jpl


@jplApp.delete("/users/{voetbalbond_user_id}/")
def delete_voetbalbond_user(voetbalbond_user_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    crud.delete_voetbalbond_user(db, voetbalbond_user_id=voetbalbond_user_id)
    return {"User is succesvol verwijderd."}


@jplApp.post("/ploegen/", response_model=schemas.Ploeg)
def create_ploeg(ploeg: schemas.PloegCreate, db: Session = Depends(get_db)):
    db_jpl = crud.get_ploeg_by_stamnummer(db, ploeg_stamnummer=ploeg.ploeg_stamnummer)
    if db_jpl:
        raise HTTPException(status_code=400, detail="Stamnummer al in gebruik.")
    return crud.create_ploeg(db=db, ploeg=ploeg)


@jplApp.get("/ploegen/", response_model=list[schemas.Ploeg])
def read_ploegen(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    ploegen = crud.get_ploegen(db, skip=skip, limit=limit)
    return ploegen


@jplApp.get("/ploeg/{ploeg_id}/", response_model=schemas.Ploeg)
def read_ploeg(ploeg_id: int, db: Session = Depends(get_db)):
    db_jpl = crud.get_ploeg(db, ploeg_id=ploeg_id)
    if db_jpl is None:
        raise HTTPException(status_code=404, detail="ID niet gevonden")
    return db_jpl


@jplApp.put("/ploeg/{ploeg_id}/", response_model=schemas.Ploeg)
def update_ploeg(ploeg_id: int, ploeg: schemas.PloegCreate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return crud.update_ploeg(db=db, ploeg=ploeg, ploeg_id=ploeg_id)


@jplApp.delete("/ploeg/{ploeg_id}/")
def delete_ploeg(ploeg_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    crud.delete_ploeg(db, ploeg_id=ploeg_id)
    return {"Ploeg is succesvol verwijderd."}


@jplApp.post("/ploeg/{ploeg_id}/trainer/", response_model=schemas.Trainer)
def create_trainer(
    ploeg_id: int, trainer: schemas.TrainerCreate, db: Session = Depends(get_db)
):
    return crud.create_trainer(db=db, trainer=trainer, ploeg_id=ploeg_id)


@jplApp.get("/trainers/", response_model=list[schemas.Trainer])
def read_trainers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    trainers = crud.get_trainers(db, skip=skip, limit=limit)
    return trainers


@jplApp.put("/trainers/{trainer_id}/", response_model=schemas.Trainer)
def update_trainer(trainer_id: int, trainer: schemas.TrainerCreate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return crud.update_trainer(db=db, trainer=trainer, trainer_id=trainer_id)


@jplApp.delete("/trainers/{trainer_id}/")
def delete_trainer(trainer_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    crud.delete_trainer(db, trainer_id=trainer_id)
    return {"Trainer is succesvol verwijderd."}


@jplApp.post("/ploeg/{ploeg_id}/stadion/", response_model=schemas.Stadion)
def create_stadion(
    ploeg_id: int, stadion: schemas.StadionCreate, db: Session = Depends(get_db)
):
    return crud.create_stadion(db=db, stadion=stadion, ploeg_id=ploeg_id)


@jplApp.get("/stadions/", response_model=list[schemas.Stadion])
def read_stadions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    stadions = crud.get_stadions(db, skip=skip, limit=limit)
    return stadions


@jplApp.put("/stadion/{stadion_id}/", response_model=schemas.Stadion)
def update_stadion(stadion_id: int, stadion: schemas.StadionCreate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return crud.update_stadion(db=db, stadion=stadion, stadion_id=stadion_id)


@jplApp.delete("/stadion/{stadion_id}/")
def delete_stadion(stadion_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    crud.delete_stadion(db, stadion_id=stadion_id)
    return {"Stadion is succesvol verwijderd."}
