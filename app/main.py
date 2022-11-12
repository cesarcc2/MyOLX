from re import search
from fastapi import FastAPI
import models.search as SearchModel
from config.config import engine
import routers.search as SearchRouter

SearchModel.Base.metadata.create_all(bind=engine)

app = FastAPI();

@app.get('/')
async def Home():
    return "Welcome Home"

app.include_router(SearchRouter.router, prefix="/search", tags=["search"])