import requests
from typing import List
from fastapi import HTTPException
from env import VSSA_API
from schemas.player import PlayerBase, PlayerResponse


async def get_players(user_id: str) -> List[PlayerResponse]:
    try:
        response = requests.get(
            f'{VSSA_API}/players?user_id={user_id}')
        data = response.json()
        players = [PlayerResponse(**item) for item in data]
    except TimeoutError:
        raise HTTPException(status_code=408,
                            detail='Timeout')
    except Exception:
        raise HTTPException(status_code=404,
                            detail='No players found')
    return players


async def create_player(player: PlayerBase) -> PlayerResponse:
    try:
        json = player.dict()
        response = requests.post(
            f'{VSSA_API}/players', json=json)
        data = response.json()
        player = PlayerResponse(**data)
    except Exception:
        raise HTTPException(status_code=404,
                            detail='No players found')
    return player


async def delete_player(user_id: str, player_id: str) -> bool:
    try:
        response = requests.delete(
            f'{VSSA_API}/players/?user_id={user_id}&player_id={player_id}')
        data = response.json()
        player = PlayerResponse(**data)
    except Exception:
        raise HTTPException(status_code=404,
                            detail='No players found')
    return player


async def update_player(user_id: str, player_id: str, player: PlayerBase) -> PlayerResponse:
    try:
        json = player.dict()
        response = requests.put(
            f'{VSSA_API}/players/?user_id={user_id}&player_id={player_id}', json=json)
        data = response.json()
        player = PlayerResponse(**data)
    except Exception:
        raise HTTPException(status_code=404,
                            detail='No players found')
    return player
