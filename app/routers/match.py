from typing import List
from fastapi import APIRouter

from schemas.match import MatchResponse, MatchPostRequest
import cruds.match as crud_match


match_router = APIRouter()


@match_router.get('/', response_model=List[MatchResponse])
async def get_matches(
        user_id: str,
        skip: int = 0,
        limit: int = 100):
    items = await crud_match.get_matches(
        user_id=user_id,
        skip=skip,
        limit=limit)
    return items


@match_router.post('/', response_model=MatchResponse)
async def create_match(match: MatchPostRequest):
    item = await crud_match.create_match(match=match)
    return item


@match_router.get('/{match_id}',
                  response_model=MatchResponse)
async def get_match(
        user_id: str,
        match_id: str):
    item = await crud_match.get_matche(
        user_id=user_id,
        match_id=match_id)
    return item
