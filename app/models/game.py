from pydantic import BaseModel

class Game(BaseModel):
    id: int
    name: str
    released: str | None = None
    rating: float | None = None
    background_image: str | None = None