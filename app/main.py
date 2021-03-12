import uvicorn
from fastapi import FastAPI, status
from routers.users import users_router

app = FastAPI(title='api', docs_url=None, openapi_url=None)


@app.get("/")
async def health_check(status_code=status.HTTP_200_OK):
    return {'message': 'OK'}

app.include_router(
    users_router,
    tags=["users"],
)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=80)
