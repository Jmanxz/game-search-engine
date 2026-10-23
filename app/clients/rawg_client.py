import os
import httpx
from dotenv import load_dotenv

load_dotenv()

class RAWGClient:
    BASE_URL = "https://api.rawg.io/api"
    
    def __init__(self):
        self.api_key = os.getenv("RAWG_API_KEY")
        
        if not self.api_key:
            raise ValueError("API Key missing!")
    
    async def search_games(
        self,
        search: str,
        page_size: int = 10,
    ) -> dict:
        url = f"{self.BASE_URL}/games"

        params = {
            "key": self.api_key,
            "search": search,
            "page_size": page_size,
        }

        async with httpx.AsyncClient(timeout=15.0) as client:
            reponse = await client.get(url, params=params)
            reponse.raise_for_status()
            return reponse.json()
    
