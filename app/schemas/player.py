from pydantic import BaseModel
from uuid import UUID


class PlayerBase(BaseModel):
    name: str
    player_number: int
    code: str
    postion: str
    weight: int
    height: int
    user_id: str
    team_id: str
    season_id: str

    class Config:
        orm_mode = True


class PlayerCreate(PlayerBase):
    uuid: str


class PlayerGet(PlayerBase):
    uuid: str


class PlayerDelete(PlayerBase):
    uuid: str


class PlayerUpdate(PlayerBase):
    uuid: str


class PlayerResponse(PlayerBase):
    uuid: str
