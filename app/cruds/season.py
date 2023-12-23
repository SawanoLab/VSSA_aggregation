import requests
from typing import List
from fastapi import HTTPException
from env import VSSA_API
from schemas.season import SeasonResponse, SeasonCreate, SeasonBase


async def get_seasons(user_id: str) -> List[SeasonResponse]:
    try:
        response = requests.get(f'{VSSA_API}/seasons/?user_id={user_id}')
        data = response.json()
        seasons = [SeasonResponse(**item) for item in data]
    except TimeoutError:
        raise HTTPException(status_code=408,
                            detail='Timeout')
    except Exception:
        raise HTTPException(status_code=404,
                            detail='No seasons found')
    return seasons


async def create_season(season: SeasonBase) -> SeasonResponse:
    try:
        json = season.dict()
        json['start_day'] = str(json['start_day'])
        json['end_day'] = str(json['end_day'])
        response = requests.post(
            f'{VSSA_API}/seasons', json=json)
        data = response.json()
        season = SeasonResponse(**data)
    except Exception:
        raise HTTPException(status_code=404,
                            detail='No seasons found')
    return season


async def delete_season(user_id: str, season_id: str) -> SeasonResponse:
    try:
        response = requests.delete(
            f'{VSSA_API}/seasons/{season_id}?user_id={user_id}')
        data = response.json()
        season = SeasonResponse(**data)
    except Exception:
        raise HTTPException(status_code=404,
                            detail='No seasons found')
    return season


async def update_season(user_id: str, season_id: str, season: SeasonCreate) -> SeasonResponse:
    try:
        json = season.dict()
        response = requests.put(
            f'{VSSA_API}/seasons/{season_id}?user_id={user_id}',
            json=json)
        data = response.json()
        season = SeasonResponse(**data)
    except Exception:
        raise HTTPException(status_code=404,
                            detail='No seasons found')
    return season
