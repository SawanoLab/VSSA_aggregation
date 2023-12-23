from pydantic import BaseModel
from uuid import UUID
from enums.attack import AttackBallType, AttackSkill, AttackEvaluationType


class AttackBase(BaseModel):
    home_team_score: int
    away_team_score: int

    home_team_set_score: int
    away_team_set_score: int

    attack_start_zone: int
    attack_end_zone: int

    attack_ball_type: AttackBallType
    attack_skill: AttackSkill
    attack_evaluation: AttackEvaluationType

    user_id: str
    match_id: str
    team_id: str
    player_id: str

    class Config:
        orm_mode = True


class AttackResponse(AttackBase):
    uuid: str
