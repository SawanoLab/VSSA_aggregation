from auth.auth import get_current_user
from fastapi import APIRouter, Depends
from typing import List

from schemas.attack import AttackResponse, AttackBase
import cruds.attack as crud_attack


attack_router = APIRouter()


@attack_router.get('/', response_model=List[AttackResponse])
async def get_attacks(
        match_id: str,
        user_id: str = Depends(get_current_user)
):

    items = await crud_attack.get_attacks(
        user_id=user_id,
        match_id=match_id)
    return items


@attack_router.post('/', response_model=AttackResponse)
async def create_attack(
    attack: AttackBase
):
    item = await crud_attack.create_attack(attack)
    return item


@attack_router.delete('/{attack_id}', response_model=AttackResponse)
async def delete_attack(
    attack_id: str,
    user_id: str = Depends(get_current_user)
):
    item = await crud_attack.delete_attack(
        user_id=user_id,
        attack_id=attack_id)
    return item
