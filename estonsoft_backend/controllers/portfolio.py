from fastapi import APIRouter, HTTPException
from typing import List
from models.portfolio import Portfolio, PortfolioResponse
from services.portfolio import PortfolioService

router = APIRouter()

@router.post("/", response_model=PortfolioResponse)
def create_post(portfolio_post: Portfolio):
    post_dict = portfolio_post.model_dump()
    created_post = PortfolioService.create_post(post_dict)
    return created_post

@router.get("/", response_model=List[PortfolioResponse])
def get_posts():
    return PortfolioService.get_all_posts()

@router.get("/{post_id}", response_model=PortfolioResponse)
def get_post(post_id: str):
    post = PortfolioService.get_post_by_id(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.put("/{post_id}", response_model=PortfolioResponse)
def update_post(post_id: str, portfolio_post: Portfolio):
    update_data = portfolio_post.model_dump(exclude_unset=True)
    updated_post = PortfolioService.update_post(post_id, update_data)
    if not updated_post:
        raise HTTPException(status_code=404, detail="Post not found")
    return updated_post

@router.delete("/{post_id}", response_model=PortfolioResponse)
def delete_post(post_id: str):
    deleted_post = PortfolioService.delete_post(post_id)
    if not deleted_post:
        raise HTTPException(status_code=404, detail="Post not found")
    return deleted_post
