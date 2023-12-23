import os
from fastapi import FastAPI, APIRouter, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware

from routers.season import season_router
from routers.team import team_router
from routers.player import player_router
from routers.match import match_router
from routers.attack import attack_router

router = APIRouter()


router.include_router(
    season_router,
    prefix='/seasons',
    tags=['seasons']
)

router.include_router(
    team_router,
    prefix='/teams',
    tags=['teams']
)

router.include_router(
    player_router,
    prefix='/players',
    tags=['players']
)

router.include_router(
    match_router,
    prefix='/matches',
    tags=['matches']
)

router.include_router(
    attack_router,
    prefix='/attacks',
    tags=['attacks']
)

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def handler(request: Request, exc: RequestValidationError):
    """
    Handles validation errors
    """
    print(exc)
    return JSONResponse(content={}, status_code=status.HTTP_400_BAD_REQUEST)


origins = [os.environ.get('ALLOW_ORIGIN')]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(router)
