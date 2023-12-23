from fastapi import APIRouter
from typing import List

from schemas.attack import AttackResponse, AttackBase
import cruds.attack as crud_attack


attack_router = APIRouter()


@attack_router.get('/', response_model=List[AttackResponse])
async def get_attacks(
        user_id: str,
        match_id: str):
    items = await crud_attack.get_attacks(
        user_id=user_id,
        match_id=match_id)
    return items


@attack_router.post('/', response_model=AttackResponse)
async def create_attack(attack: AttackBase):
    item = await crud_attack.create_attack(attack)
    return item


@attack_router.delete('/{attack_id}', response_model=AttackResponse)
async def delete_attack(user_id: str, attack_id: str):
    item = await crud_attack.delete_attack(
        user_id=user_id,
        attack_id=attack_id)
    return item
