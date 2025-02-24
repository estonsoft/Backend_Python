from pydantic import BaseModel, HttpUrl
from typing import Optional
from bson import ObjectId

class Testimonial(BaseModel):
  star: int         
  name: str       
  image: str
  content: str    
  designation: str 


class TestimonialResponse(Testimonial):
    id: str  

