from auth.auth import get_current_user
import cruds.season as crud_season
from fastapi import APIRouter, Depends
from schemas.season import SeasonResponse, SeasonBase, SeasonCreate
from typing import List


season_router = APIRouter()


@season_router.get('/', response_model=List[SeasonResponse])
async def get_seasons(
    user_id: str = Depends(get_current_user)
):
    items = await crud_season.get_seasons(user_id=user_id)
    return items


@season_router.post("/", response_model=SeasonResponse)
async def create_season(
    season: SeasonBase
):
    item = await crud_season.create_season(season)
    return item


@ season_router.delete("/{season_id}", response_model=SeasonResponse)
async def delete_season(
        season_id: str,
        user_id: str = Depends(get_current_user)
):
    item = await crud_season.delete_season(
        user_id=user_id,
        season_id=season_id)
    return item


@season_router.put("/{season_id}", response_model=SeasonResponse)
async def update_season(
        season_id: str,
        season: SeasonCreate,
        user_id: str = Depends(get_current_user),
):
    item = await crud_season.update_season(
        user_id=user_id,
        season_id=season_id,
        season=season)
    return item
