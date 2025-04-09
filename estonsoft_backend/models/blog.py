from pydantic import BaseModel
from typing import List


class BlogPost(BaseModel):
    title: str
    image: str
    paragraph: str
    content: str
    authorName:str
    authorImage:str
    authorDesignation:str
    tags: List[str]
    publishDate: str

class BlogPostResponse(BlogPost):
    id: str
