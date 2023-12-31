import requests
from typing import List
from fastapi import HTTPException
from env import VSSA_API
from schemas.match import MatchResponse, MatchPostRequest


async def get_matches(
        user_id: str,
        skip: int = 0,
        limit: int = 100) -> List[MatchResponse]:
    try:
        response = requests.get(
            f'{VSSA_API}/matches?user_id={user_id}&skip={skip}&limit={limit}')
        data = response.json()
        matches = [MatchResponse(**item) for item in data]
    except TimeoutError:
        raise HTTPException(status_code=408,
                            detail='Timeout')
    except Exception:
        raise HTTPException(status_code=404,
                            detail='No matches found')
    return matches


async def create_match(match: MatchPostRequest) -> MatchResponse:
    try:
        json = match.dict()
        response = requests.post(
            f'{VSSA_API}/matches', json=json)
        data = response.json()
    except Exception:
        raise HTTPException(status_code=404,
                            detail='No matches found')
    return data


async def get_matche(
        user_id: str,
        match_id: str) -> MatchResponse:
    try:
        response = requests.get(
            f'{VSSA_API}/matches/{match_id}?user_id={user_id}')
        data = response.json()
        match = MatchResponse(**data)
    except TimeoutError:
        raise HTTPException(status_code=408,
                            detail='Timeout')
    except Exception:
        raise HTTPException(status_code=404,
                            detail='No matches found')
    return match


async def delete_match(
        user_id: str,
        match_id: str) -> str:
    try:
        response = requests.delete(
            f'{VSSA_API}/matches/{match_id}?user_id={user_id}')
        data = response.json()
        return data
    except Exception:
        raise HTTPException(status_code=404,
                            detail='No matches found')
