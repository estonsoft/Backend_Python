from repositories.blog import BlogRepository

class BlogService:
    @staticmethod
    def create_post(blog_post: dict):
        return BlogRepository.create(blog_post)

    @staticmethod
    def get_all_posts():
        return BlogRepository.get_all()

    @staticmethod
    def get_post_by_id(post_id: str):
        return BlogRepository.get_by_id(post_id)

    @staticmethod
    def update_post(post_id: str, update_data: dict):
        return BlogRepository.update(post_id, update_data)

    @staticmethod
    def delete_post(post_id: str):
        return BlogRepository.delete(post_id)
