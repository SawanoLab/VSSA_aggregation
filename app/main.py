from fastapi import APIRouter, FastAPI


router = APIRouter()


@router.get('/')
async def hello_world():
    return {'message': 'Hello World!'}


app = FastAPI()

app.include_router(router)
