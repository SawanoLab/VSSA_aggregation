from fastapi import APIRouter
from schemas.player import PlayerResponse, PlayerBase
from typing import List
import cruds.player as crud_team


player_router = APIRouter()


@player_router.get('/', response_model=List[PlayerResponse])
async def get_players(user_id: str):
    items = await crud_team.get_players(user_id=user_id)
    return items


@player_router.post('/', response_model=PlayerResponse)
async def create_player(player: PlayerBase):
    item = await crud_team.create_player(player)
    return item


@player_router.delete('/', response_model=PlayerResponse)
async def delete_player(
        user_id: str,
        player_id: str):
    item = await crud_team.delete_player(
        user_id=user_id,
        player_id=player_id)
    return item


@player_router.put('/{player_id}', response_model=PlayerResponse)
async def update_player(
        user_id: str,
        player_id: str,
        player: PlayerBase):
    item = await crud_team.update_player(
        user_id=user_id,
        player_id=player_id,
        player=player)
    return item
