import typing as t
from fastapi import APIRouter, Response, status
from schemas.user import UserOut

users_router = r = APIRouter()


@r.get("/users", response_model=t.List[UserOut], status_code=status.HTTP_200_OK)
async def users_list(response: Response):
    response = []
    response.append(UserOut(id=1, name='hoge', email='hoge@test.com'))
    response.append(UserOut(id=2, name='fuga', email='fuga@test.com'))
    return response
