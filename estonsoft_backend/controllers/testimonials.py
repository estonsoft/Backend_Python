from fastapi import APIRouter, Depends
from services.testimonials import TestimonialService
from models.testimonials import Testimonial, TestimonialResponse
from typing import List
from lib.jwt import verify_token

router = APIRouter(prefix="/testimonials", tags=["Testimonials"])

@router.post("/", response_model=dict)
async def create_testimonial(testimonial: Testimonial, auth_user: dict = Depends(verify_token)):
    return TestimonialService.create_testimonial(testimonial, auth_user)

@router.get("/", response_model=List[TestimonialResponse])
async def get_all_testimonials(auth_user: dict = Depends(verify_token)):
    return TestimonialService.get_all_testimonials(auth_user)

@router.get("/{testimonial_id}", response_model=TestimonialResponse)
async def get_testimonial(testimonial_id: str, auth_user: dict = Depends(verify_token)):
    return TestimonialService.get_testimonial_by_id(testimonial_id, auth_user)

@router.put("/{testimonial_id}", response_model=dict)
async def update_testimonial(testimonial_id: str, updated_testimonial: Testimonial, auth_user: dict = Depends(verify_token)):
    return TestimonialService.update_testimonial(testimonial_id, updated_testimonial, auth_user)

@router.delete("/{testimonial_id}", response_model=dict)
async def delete_testimonial(testimonial_id: str, auth_user: dict = Depends(verify_token)):
    return TestimonialService.delete_testimonial(testimonial_id, auth_user)
