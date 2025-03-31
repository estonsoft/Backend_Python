from fastapi import APIRouter, HTTPException, Depends
from typing import List
from models.user import UserCreate, UserResponse
from services.user import UserService
from lib.jwt import verify_token

router = APIRouter(prefix="/users")

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, auth_user: dict = Depends(verify_token)):
    if "create_user" not in auth_user["permissions"]:
        raise HTTPException(status_code=403, detail="❌ Permission denied: You cannot create a user")

    if UserService.get_user_by_email(user.email):
        raise HTTPException(status_code=400, detail="❌ Email already registered")

    return UserService.create_user(user.dict())

@router.get("/", response_model=List[UserResponse])
def get_users(auth_user: dict = Depends(verify_token)):
    if "view_users" not in auth_user["permissions"]:
        raise HTTPException(status_code=403, detail="❌ Permission denied")
    
    return UserService.get_all_users()

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: str, auth_user: dict = Depends(verify_token)):
    if "view_users" not in auth_user["permissions"]:
        raise HTTPException(status_code=403, detail="❌ Permission denied")

    user = UserService.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="❌ User not found")
    return user

@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: str, user: UserCreate, auth_user: dict = Depends(verify_token)):
    if "update_user" not in auth_user["permissions"]:
        raise HTTPException(status_code=403, detail="❌ Permission denied")

    updated_user = UserService.update_user(user_id, user.dict())
    if not updated_user:
        raise HTTPException(status_code=404, detail="❌ User not found")
    return updated_user

@router.delete("/{user_id}", response_model=UserResponse)
def delete_user(user_id: str, auth_user: dict = Depends(verify_token)):
    if "delete_user" not in auth_user["permissions"]:
        raise HTTPException(status_code=403, detail="❌ Permission denied")

    deleted_user = UserService.delete_user(user_id)
    if not deleted_user:
        raise HTTPException(status_code=404, detail="❌ User not found")
    return deleted_user
