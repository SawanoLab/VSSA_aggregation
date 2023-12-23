from typing import Dict, Optional
from pydantic import BaseModel


class PlayerInfo(BaseModel):
    uuid: str
    name: str
    player_number: int
    code: str
    postion: str
    weight: Optional[int]
    height: Optional[int]


class TeamPlayers(BaseModel):
    PlayerInfo: PlayerInfo
    onCourt: bool
    zone_code: Optional[str]
    libero: Optional[bool]


class TeamRequest(BaseModel):
    uuid: str
    team_name: str
    players: Dict[str, TeamPlayers]
    setter_postion: str


class MatchResponse(BaseModel):
    uuid: str
    home_team: TeamRequest
    away_team: TeamRequest
    season_name: str
    youtube_url: str


class PlayerMatchInfo(BaseModel):
    player_id: str
    on_court: bool
    zone_code: Optional[str]
    libero: Optional[bool]


class Match(BaseModel):
    home_team_id: str
    away_team_id: str
    user_id: str
    season_id: str
    youtube_url: str


class MatchRequest(BaseModel):
    uuid: str
    home_team: TeamRequest
    away_team: TeamRequest
    season_name: str
    youtube_url: str


class MatchPostRequest(BaseModel):
    Match: Match
    PlayerMatchInfo: Dict[str, PlayerMatchInfo]
