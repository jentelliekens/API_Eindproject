from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer

import schemas
import models
import auth

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_voetbalbond_user(db: Session, voetbalbond_user_id: int):
    return db.query(models.User).filter(models.User.voetbalbond_user_id == voetbalbond_user_id).first()


def get_voetbalbond_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_voetbalbond_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_voetbalbond_user(db: Session, voetbalbond_user: schemas.UserCreate):
    hashed_password = auth.get_password_hash(voetbalbond_user.password)
    db_jpl = models.User(email=voetbalbond_user.email, hashed_password=hashed_password)
    db.add(db_jpl)
    db.commit()
    db.refresh(db_jpl)
    return db_jpl


def delete_voetbalbond_user(db: Session, voetbalbond_user_id: int):
    db.query(models.User).filter(models.User.voetbalbond_user_id == voetbalbond_user_id).delete()
    db.commit()


def get_ploeg(db: Session, ploeg_id: int):
    return db.query(models.Ploeg).filter(models.Ploeg.ploeg_id == ploeg_id).first()


def get_ploeg_by_stamnummer(db: Session, ploeg_stamnummer: int):
    return db.query(models.Ploeg).filter(models.Ploeg.ploeg_stamnummer == ploeg_stamnummer).first()


def get_ploegen(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Ploeg).offset(skip).limit(limit).all()


def delete_ploeg(db: Session, ploeg_id: int):
    db.query(models.Ploeg).filter(models.Ploeg.ploeg_id == ploeg_id).delete()
    db.commit()


def create_ploeg(db: Session, ploeg: schemas.PloegCreate):
    db_jpl = models.Ploeg(ploeg_stamnummer=ploeg.ploeg_stamnummer, ploeg_naam=ploeg.ploeg_naam, ploeg_stand=ploeg.ploeg_stand)
    db.add(db_jpl)
    db.commit()
    db.refresh(db_jpl)
    return db_jpl


def update_ploeg(db: Session, ploeg: schemas.PloegCreate, ploeg_id: int):
    db_jpl = get_ploeg(db=db, ploeg_id=ploeg_id)
    db_jpl.ploeg_stand = ploeg.ploeg_stand
    db_jpl.ploeg_stamnummer = ploeg.ploeg_stamnummer
    db_jpl.ploeg_naam = ploeg.ploeg_naam
    db.commit()
    db.refresh(db_jpl)
    return db_jpl


def get_trainer_by_name(db: Session, trainer_naam: str):
    return db.query(models.Trainers).filter(models.Trainers.trainer_naam == trainer_naam).first()


def get_trainers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Trainers).offset(skip).limit(limit).all()


def get_trainer(db: Session, trainer_id: int):
    return db.query(models.Trainers).filter(models.Trainers.trainer_id == trainer_id).first()


def create_trainer(db: Session, trainer: schemas.TrainerCreate, ploeg_id: int):
    db_jpl = models.Trainers(**trainer.dict(), ploeg_id=ploeg_id)
    db.add(db_jpl)
    db.commit()
    db.refresh(db_jpl)
    return db_jpl


def update_trainer(db: Session, trainer: schemas.TrainerCreate, trainer_id: int):
    db_jpl = get_trainer(db=db, trainer_id=trainer_id)
    db_jpl.trainer_naam = trainer.trainer_naam
    db_jpl.trainer_leeftijd = trainer.trainer_leeftijd
    db_jpl.trainer_nationaliteit = trainer.trainer_nationaliteit
    db.commit()
    db.refresh(db_jpl)
    return db_jpl


def delete_trainer(db: Session, trainer_id: int):
    db.query(models.Trainers).filter(models.Trainers.trainer_id == trainer_id).delete()
    db.commit()


def get_stadion_by_name(db: Session, stadion_naam: str):
    return db.query(models.Stadion).filter(models.Stadion.stadion_naam == stadion_naam).first()


def get_stadions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Stadion).offset(skip).limit(limit).all()


def get_stadion(db: Session, stadion_id: int):
    return db.query(models.Stadion).filter(models.Stadion.stadion_id == stadion_id).first()


def create_stadion(db: Session, stadion: schemas.StadionCreate, ploeg_id: int):
    db_jpl = models.Stadion(**stadion.dict(), ploeg_id=ploeg_id)
    db.add(db_jpl)
    db.commit()
    db.refresh(db_jpl)
    return db_jpl


def update_stadion(db: Session, stadion: schemas.StadionCreate, stadion_id: int):
    db_jpl = get_stadion(db=db, stadion_id=stadion_id)
    db_jpl.stadion_bouwjaar = stadion.stadion_bouwjaar
    db_jpl.stadion_naam = stadion.stadion_naam
    db_jpl.stadion_capaciteit = stadion.stadion_capaciteit
    db.commit()
    db.refresh(db_jpl)
    return db_jpl


def delete_stadion(db: Session, stadion_id: int):
    db.query(models.Stadion).filter(models.Stadion.stadion_id == stadion_id).delete()
    db.commit()
