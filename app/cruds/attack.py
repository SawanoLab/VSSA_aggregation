import requests
from typing import List
from fastapi import HTTPException
from env import VSSA_API
from schemas.attack import AttackBase, AttackResponse


async def get_attacks(user_id: str, match_id: str) -> List[AttackResponse]:
    try:
        response = requests.get(
            f'{VSSA_API}/attacks?user_id={user_id}&match_id={match_id}')
        data = response.json()
        attacks = [AttackResponse(**item) for item in data]
    except TimeoutError:
        raise HTTPException(status_code=408,
                            detail='Timeout')

    except Exception:
        raise HTTPException(status_code=404,
                            detail='No attacks found')
    return attacks


async def create_attack(attack: AttackBase) -> AttackResponse:
    try:
        json = attack.dict()
        response = requests.post(
            f'{VSSA_API}/attacks', json=json)
        data = response.json()
        attack = AttackResponse(**data)
    except Exception:
        raise HTTPException(status_code=404,
                            detail='No attacks found')
    return attack


async def delete_attack(user_id: str, attack_id: str) -> AttackResponse:
    try:
        response = requests.delete(
            f'{VSSA_API}/attacks/{attack_id}?user_id={user_id}')
        data = response.json()
        attack = AttackResponse(**data)
    except Exception:
        raise HTTPException(status_code=404,
                            detail='No attacks found')
    return attack
