from pydantic import BaseModel, HttpUrl
from typing import Optional
from bson import ObjectId

class Portfolio(BaseModel):
    title: str
    description: Optional[str] = None
    image: str
    link: str   


class PortfolioResponse(Portfolio):
    id: str  

