from repositories.testimonial import TestimonialRepository

class TestimonialService:
    @staticmethod
    def create_post(testimonial_post: dict):
        return TestimonialRepository.create(testimonial_post)

    @staticmethod
    def get_all_posts():
        return TestimonialRepository.get_all()

    @staticmethod
    def get_post_by_id(post_id: str):
        return TestimonialRepository.get_by_id(post_id)

    @staticmethod
    def update_post(post_id: str, update_data: dict):
        return TestimonialRepository.update(post_id, update_data)

    @staticmethod
    def delete_post(post_id: str):
        return TestimonialRepository.delete(post_id)
