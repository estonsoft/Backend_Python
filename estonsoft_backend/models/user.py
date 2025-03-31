from pydantic import BaseModel
from typing import List, Optional

class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    permissions: Optional[List[str]] = []

class UserResponse(BaseModel):
    id: str
    name: Optional[str] = None  # Now optional
    email: Optional[str] = None  # Now optional
    permissions: Optional[List[str]] = []  # Now optional

