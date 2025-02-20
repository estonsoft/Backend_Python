from fastapi import APIRouter, HTTPException
from typing import List
from models.blog import BlogPost, BlogPostResponse
from services.blog import BlogService

router = APIRouter()

@router.post("/", response_model=BlogPostResponse)
def create_post(blog_post: BlogPost):
    post_dict = blog_post.model_dump()
    created_post = BlogService.create_post(post_dict)
    return created_post

@router.get("/", response_model=List[BlogPostResponse])
def get_posts():
    return BlogService.get_all_posts()

@router.get("/{post_id}", response_model=BlogPostResponse)
def get_post(post_id: str):
    post = BlogService.get_post_by_id(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.put("/{post_id}", response_model=BlogPostResponse)
def update_post(post_id: str, blog_post: BlogPost):
    update_data = blog_post.model_dump(exclude_unset=True)
    updated_post = BlogService.update_post(post_id, update_data)
    if not updated_post:
        raise HTTPException(status_code=404, detail="Post not found")
    return updated_post

@router.delete("/{post_id}", response_model=BlogPostResponse)
def delete_post(post_id: str):
    deleted_post = BlogService.delete_post(post_id)
    if not deleted_post:
        raise HTTPException(status_code=404, detail="Post not found")
    return deleted_post
