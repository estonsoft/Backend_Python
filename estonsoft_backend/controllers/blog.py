from fastapi import APIRouter, Depends, HTTPException
from models.blog import BlogPost, BlogPostResponse
from services.blog import BlogService
from lib.jwt import verify_token
from typing import List

router = APIRouter(prefix="/blogs")

@router.get("/health", response_model=dict)
def health_check():
    return {"status": "ok"}


@router.post("/", response_model=dict)
def create_blog(blog: BlogPost, auth_user: dict = Depends(verify_token)):
    return BlogService.create_blog(blog.dict(), auth_user)

@router.put("/{blog_id}", response_model=dict)
def update_blog(blog_id: str, blog: BlogPost, auth_user: dict = Depends(verify_token)):
    return BlogService.update_blog(blog_id, blog.dict(), auth_user)

@router.delete("/{blog_id}", response_model=dict)
def delete_blog(blog_id: str, auth_user: dict = Depends(verify_token)):
    return BlogService.delete_blog(blog_id, auth_user)

@router.get("/", response_model=List[BlogPostResponse])
def get_all_blogs(auth_user: dict = Depends(verify_token)):
    return BlogService.get_all_blogs(auth_user)

@router.get("/{blog_id}", response_model=BlogPostResponse)
def get_blog_by_id(blog_id: str, auth_user: dict = Depends(verify_token)):
    return BlogService.get_blog_by_id(blog_id, auth_user)
