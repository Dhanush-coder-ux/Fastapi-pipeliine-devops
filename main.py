from fastapi import FastAPI
from api.todo import router
from database.main import ENGINE,BASE

app = FastAPI()
app.include_router(router)


@app.get("/")
async def root():
    return {"message": "API is running!"}

@app.on_event("startup")
async def onstart_up():
    async with ENGINE.begin() as s:
        await s.run_sync(BASE.metadata.create_all)