from fastapi import APIRouter, HTTPException
from bson import ObjectId
from datetime import datetime
from .database import postCollection
from .models import BlogPost, BlogPostResponse
from typing import List

router = APIRouter()

@router.post("/post/", response_model=BlogPostResponse)
def create_post(blog_post: BlogPost):
    post_dict = blog_post.dict()
    post_dict["timestamp"] = datetime.now().isoformat()
    result = postCollection.insert_one(post_dict)
    post_dict["id"] = str(result.inserted_id)
    return post_dict

@router.get("/posts/", response_model=List[BlogPostResponse])
def get_posts():
    posts = []
    for post in postCollection.find():
        post["id"] = str(post.pop("_id"))
        posts.append(post)
    return posts

@router.get("/post/{post_id}", response_model=BlogPostResponse)
def get_post(post_id: str):
    post_object_id = ObjectId(post_id)
    post = postCollection.find_one({"_id": post_object_id})
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    post["id"] = str(post.pop("_id"))
    return post

@router.put("/post/{post_id}", response_model=BlogPostResponse)
def update_post(post_id: str, blog_post: BlogPost):
    post_object_id = ObjectId(post_id)
    existing_post = postCollection.find_one({"_id": post_object_id})
    if not existing_post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    update_data = blog_post.dict(exclude_unset=True)
    update_data["timestamp"] = existing_post["timestamp"]
    
    postCollection.update_one({"_id": post_object_id}, {"$set": update_data})
    
    updated_post = postCollection.find_one({"_id": post_object_id})
    updated_post["id"] = str(updated_post.pop("_id"))
    return updated_post

@router.delete("/post/{post_id}", response_model=BlogPostResponse)
def delete_post(post_id: str):
    post_object_id = ObjectId(post_id)
    existing_post = postCollection.find_one({"_id": post_object_id})
    if not existing_post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    postCollection.delete_one({"_id": post_object_id})
    
    existing_post["id"] = str(existing_post.pop("_id"))
    return existing_post
