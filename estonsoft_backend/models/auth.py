from pydantic import BaseModel

class UserLogin(BaseModel):
    """User login request model"""
    email: str
    password: str

class TokenResponse(BaseModel):
    """Response model for login with JWT token"""
    token: str
    message: str
