from pydantic import BaseModel
from typing import List

class BlogPost(BaseModel):
    title: str
    image: str
    paragraph: str
    content: str
    author: str
    tags: List[str]
    publishDate: str

class BlogPostResponse(BlogPost):
    id: str
