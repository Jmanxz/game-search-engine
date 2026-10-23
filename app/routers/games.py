from fastapi import APIRouter, HTTPException, Query
from app.models.game import Game
from app.services.search import SearchService

router = APIRouter(prefix="/games", tags=["Games"])

@router.get("/search",response_model=list[Game])
async def search_games(q: str = Query(min_length=1)):
    try:
        service = SearchService()
        return await service.search(q)
    except Exception as exc:
        raise HTTPException(
            status_code=502,
            detail=f"Game search failed: {exc}",
        ) from exc
