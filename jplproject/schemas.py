from pydantic import BaseModel


class TrainerBase(BaseModel):
    trainer_naam: str
    trainer_leeftijd: int
    trainer_nationaliteit: str

    class Config:
        orm_mode = True


class Trainer(TrainerBase):
    trainer_id: int
    ploeg_id: int


class TrainerCreate(TrainerBase):
    trainer_naam: str
    trainer_leeftijd: int
    trainer_nationaliteit: str


class StadionBase(BaseModel):
    stadion_bouwjaar: int
    stadion_naam: str
    stadion_capaciteit: int


class Stadion(StadionBase):
    stadion_id: int
    ploeg_id: int

    class Config:
        orm_mode = True


class StadionCreate(StadionBase):
    stadion_bouwjaar: int
    stadion_naam: str
    stadion_capaciteit: int


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    voetbalbond_user_id: int
    is_active: bool

    class Config:
        orm_mode = True


class PloegBase(BaseModel):
    ploeg_stand: int
    ploeg_stamnummer: int
    ploeg_naam: str


class Ploeg(PloegBase):
    ploeg_id: int
    trainers: list[Trainer] = []
    stadions: list[Stadion] = []

    class Config:
        orm_mode = True


class PloegCreate(PloegBase):
    ploeg_stand: int
    ploeg_stamnummer: int
    ploeg_naam: str
