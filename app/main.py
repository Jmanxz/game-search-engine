from fastapi import FastAPI
from app.routers.games import router as games_router

app = FastAPI(title="Game Search Engine")

app.include_router(games_router)

@app.get("/")
def home():
    return {"message":"Welcome to the Game Search Engine"}