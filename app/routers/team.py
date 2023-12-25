from auth.auth import get_current_user
from fastapi import APIRouter, Depends
from schemas.team import TeamBase, TeamResponse
from typing import List
import cruds.team as crud_team


team_router = APIRouter()


@team_router.get('/', response_model=List[TeamResponse])
async def get_teams(
    user_id: str = Depends(get_current_user)
):
    items = await crud_team.get_teams(user_id=user_id)
    return items


@team_router.post('/', response_model=TeamResponse)
async def create_team(team: TeamBase):
    db_team = await crud_team.create_team(team)
    return db_team


@team_router.delete('/{team_id}', response_model=TeamResponse)
async def delete_team(
    team_id: str,
    user_id: str = Depends(get_current_user)
):
    db_team = await crud_team.delete_team(
        user_id=user_id,
        team_id=team_id)
    return db_team


@team_router.put('/{team_id}', response_model=TeamResponse)
async def update_team(
    team_id: str,
    team: TeamBase,
    user_id: str = Depends(get_current_user)
):
    db_team = await crud_team.update_team(
        user_id=user_id,
        team_id=team_id,
        team=team)
    return db_team
