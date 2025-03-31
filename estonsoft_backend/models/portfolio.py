from pydantic import BaseModel
from typing import Optional

class Portfolio(BaseModel):
    title: str
    description: Optional[str] = None
    image: str
    link: str  

class PortfolioResponse(Portfolio):
    id: str  
