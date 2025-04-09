from pydantic import BaseModel
from typing import List

class Author(BaseModel):
    name: str
    image: str
    designation: str

class BlogPost(BaseModel):
    title: str
    image: str
    paragraph: str
    content: str
    author: Author
    tags: List[str]
    publishDate: str
    views: int
    comments: int
    url: str

class BlogPostResponse(BlogPost):
    id: str
