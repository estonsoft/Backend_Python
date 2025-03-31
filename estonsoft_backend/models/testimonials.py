from pydantic import BaseModel
from typing import Optional

class Testimonial(BaseModel):
    star: int         
    name: str       
    image: str
    content: str    
    designation: str 


class TestimonialResponse(Testimonial):
    id: str
    star: int         
    name: str       
    image: str
    content: str    
    designation: str 

