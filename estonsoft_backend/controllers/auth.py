from fastapi import APIRouter, HTTPException, Depends
from services.auth import AuthService
from lib.jwt import verify_token
from models.auth import TokenResponse, UserLogin
from models.user import UserResponse

router = APIRouter(prefix="/auth")

@router.post("/login", response_model=TokenResponse)
def login(user: UserLogin):
    """Authenticate user and return JWT token"""
    response = AuthService.login(user.email, user.password)
    if not response:
        raise HTTPException(status_code=400, detail="❌ Invalid email or password")
    return response

@router.get("/me/", response_model=UserResponse)
def get_me(auth_user: dict = Depends(verify_token)):
    """Get logged-in user information"""
    user_data = AuthService.get_user_info(auth_user["_id"])
    if not user_data:
        raise HTTPException(status_code=404, detail="❌ User not found")
    
    return {
        "id": str(user_data["_id"]),
        "name": user_data["name"],
        "email": user_data["email"],
        "permissions": user_data.get("permissions", [])
    }
