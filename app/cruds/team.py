import requests
from typing import List
from fastapi import HTTPException
from env import VSSA_API
from schemas.team import TeamResponse


async def get_teams(
        user_id: str
) -> List[TeamResponse]:
    try:
        response = requests.get(
            f'{VSSA_API}/teams?user_id={user_id}')
        data = response.json()
        teams = [TeamResponse(**item) for item in data]
    except TimeoutError:
        raise HTTPException(status_code=408,
                            detail='Timeout')
    except Exception:
        raise HTTPException(status_code=404,
                            detail='No teams found')
    return teams


async def create_team(team: TeamResponse) -> TeamResponse:
    try:
        json = team.dict()
        response = requests.post(
            f'{VSSA_API}/teams', json=json)
        data = response.json()
        team = TeamResponse(**data)
    except Exception:
        raise HTTPException(status_code=404,
                            detail='No teams found')
    return team


async def delete_team(
        user_id: str,
        team_id: str) -> TeamResponse:
    try:
        response = requests.delete(
            f'{VSSA_API}/teams/{team_id}?user_id={user_id}')
        data = response.json()
        return TeamResponse(**data)
    except Exception:
        raise HTTPException(status_code=404,
                            detail='No teams found')


async def update_team(
        user_id: str,
        team_id: str,
        team: TeamResponse) -> TeamResponse:
    try:
        json = team.dict()
        response = requests.put(
            f'{VSSA_API}/teams/{team_id}?user_id={user_id}',
            json=json)
        data = response.json()
        team = TeamResponse(**data)
    except Exception:
        raise HTTPException(status_code=404,
                            detail='No teams found')
    return team
