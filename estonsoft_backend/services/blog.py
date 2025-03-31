from fastapi import HTTPException
from bson import ObjectId
from repositories.blog import BlogRepository

class BlogService:

    @staticmethod
    def create_blog(blog_data, auth_user):
        if "create_blog" not in auth_user["permissions"]:
            raise HTTPException(status_code=403, detail="❌ Permission denied")
        
        blog_data["user_id"] = str(auth_user["_id"])
        blog_id = BlogRepository.create(blog_data)
        
        return {"id": blog_id, "message": "✅ Blog created successfully"}

    @staticmethod
    def update_blog(blog_id, update_data, auth_user):
        if "update_blog" not in auth_user["permissions"]:
            raise HTTPException(status_code=403, detail="❌ Permission denied")
        
        existing_blog = BlogRepository.get_by_id(blog_id)
        if not existing_blog:
            raise HTTPException(status_code=404, detail="❌ Blog not found")
        
        if str(existing_blog["user_id"]) != str(auth_user["_id"]):
            raise HTTPException(status_code=403, detail="❌ Unauthorized to update this blog")
        
        BlogRepository.update(blog_id, update_data)
        return {"message": "✅ Blog updated successfully"}

    @staticmethod
    def delete_blog(blog_id, auth_user):
        if "delete_blog" not in auth_user["permissions"]:
            raise HTTPException(status_code=403, detail="❌ Permission denied")

        existing_blog = BlogRepository.get_by_id(blog_id)
        if not existing_blog:
            raise HTTPException(status_code=404, detail="❌ Blog not found")

        if str(existing_blog["user_id"]) != str(auth_user["_id"]):
            raise HTTPException(status_code=403, detail="❌ Unauthorized to delete this blog")

        BlogRepository.delete(blog_id)
        return {"message": "✅ Blog deleted successfully"}

    @staticmethod
    def get_all_blogs(auth_user):
        if "read_blog" not in auth_user["permissions"]:
            raise HTTPException(status_code=403, detail="❌ Permission denied")

        blogs = BlogRepository.get_all()
        return [
            {
                "id": str(blog["_id"]),
                "title": blog["title"],
                "image": blog.get("image"),
                "paragraph": blog["paragraph"],
                "content": blog["content"],
                "author": blog["author"],
                "tags": blog.get("tags", []),
                "publishDate": blog["publishDate"]
            }
            for blog in blogs
        ]

    @staticmethod
    def get_blog_by_id(blog_id, auth_user):
        if "read_blog" not in auth_user["permissions"]:
            raise HTTPException(status_code=403, detail="❌ Permission denied")

        blog = BlogRepository.get_by_id(blog_id)
        if not blog:
            raise HTTPException(status_code=404, detail="❌ Blog not found")

        return {
            "id": str(blog["_id"]),
            "title": blog["title"],
            "image": blog.get("image"),
            "paragraph": blog["paragraph"],
            "content": blog["content"],
            "author": blog["author"],
            "tags": blog.get("tags", []),
            "publishDate": blog["publishDate"]
        }
