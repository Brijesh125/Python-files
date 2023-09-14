from pydantic import BaseModel


class Data(BaseModel):
    name: str
    directors: str
    producers: str
    casts: str
    subtitles: str
    language: str
    genres: str
    rating: float | int
    resolution: str
    release_Date: str
    revenue_Collection: str
    overall_status: str
