from app.clients.rawg_client import RAWGClient
from app.models.game import Game

class SearchService:
    
    def __init__(self):
        self.client = RAWGClient()
        
    async def search(self, query: str) -> list[Game]:
        response = await self.client.search_games(query)

        return [
            Game.model_validate(game)
            for game in response.get("results", [])
        ]