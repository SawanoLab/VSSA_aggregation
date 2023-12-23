from pydantic import BaseModel
from uuid import UUID


class TeamBase(BaseModel):
    name: str
    code: str
    director: str
    coach: str
    trainer: str
    doctor: str
    season_id: str
    user_id: str

    class Config:
        orm_mode = True


class TeamCreate(TeamBase):
    uuid: str


class TeamResponse(TeamBase):
    uuid: str
