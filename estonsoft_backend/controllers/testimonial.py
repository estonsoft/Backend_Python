from fastapi import APIRouter, HTTPException
from typing import List
from models.testimonial import Testimonial, TestimonialResponse
from services.testimonial import TestimonialService

router = APIRouter()

@router.post("/", response_model=TestimonialResponse)
def create_post(testimonial_post: Testimonial):
    post_dict = testimonial_post.model_dump()
    created_post = TestimonialService.create_post(post_dict)
    return created_post

@router.get("/", response_model=List[TestimonialResponse])
def get_posts():
    return TestimonialService.get_all_posts()

@router.get("/{post_id}", response_model=TestimonialResponse)
def get_post(post_id: str):
    post = TestimonialService.get_post_by_id(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.put("/{post_id}", response_model=TestimonialResponse)
def update_post(post_id: str, testimonial_post: Testimonial):
    update_data = testimonial_post.model_dump(exclude_unset=True)
    updated_post = TestimonialService.update_post(post_id, update_data)
    if not updated_post:
        raise HTTPException(status_code=404, detail="Post not found")
    return updated_post

@router.delete("/{post_id}", response_model=TestimonialResponse)
def delete_post(post_id: str):
    deleted_post = TestimonialService.delete_post(post_id)
    if not deleted_post:
        raise HTTPException(status_code=404, detail="Post not found")
    return deleted_post
