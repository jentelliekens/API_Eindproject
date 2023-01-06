from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class Ploeg(Base):
    __tablename__ = "ploegen"

    ploeg_id = Column(Integer, primary_key=True, index=True)
    ploeg_stand = Column(Integer, index=True , unique=True)
    ploeg_stamnummer = Column(Integer, index=True , unique=True)
    ploeg_naam = Column(String, index=True)

    trainers = relationship("Trainers", back_populates="ploegen")
    stadions = relationship("Stadion", back_populates="ploegen")

class Trainers(Base):
    __tablename__ = "trainers"

    trainer_id = Column(Integer, primary_key=True, index=True)
    trainer_naam = Column(String, index=True)
    trainer_leeftijd = Column(Integer, index=True)
    trainer_nationaliteit = Column(String, index=True)
    ploeg_id = Column(Integer, ForeignKey("ploegen.ploeg_id"))

    ploegen = relationship("Ploeg", back_populates="trainers")


class Stadion(Base):
    __tablename__ = "stadions"

    stadion_id = Column(Integer, primary_key=True, index=True)
    stadion_bouwjaar = Column(Integer, index=True , unique=True)
    stadion_naam = Column(String, index=True)
    stadion_capaciteit = Column(Integer, index=True,)
    ploeg_id = Column(Integer, ForeignKey("ploegen.ploeg_id"))

    ploegen = relationship("Ploeg", back_populates="stadions")


class User(Base):
    __tablename__ = "voetbalbond_users"

    voetbalbond_user_id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

