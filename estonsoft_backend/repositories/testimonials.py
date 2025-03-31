from bson import ObjectId
from lib.mongo import get_mongo

db = get_mongo()

class TestimonialRepository:
    collection = db["testimonials"]

    @staticmethod
    def create(testimonial_data: dict):
        """Insert a new testimonial into the database."""
        return TestimonialRepository.collection.insert_one(testimonial_data).inserted_id

    @staticmethod
    def get_all():
        """Retrieve all testimonials from the database."""
        return list(TestimonialRepository.collection.find())

    @staticmethod
    def get_by_id(testimonial_id: str):
        """Retrieve a single testimonial by ID."""
        return TestimonialRepository.collection.find_one({"_id": ObjectId(testimonial_id)})

    @staticmethod
    def update(testimonial_id: str, updated_data: dict):
        """Update an existing testimonial."""
        return TestimonialRepository.collection.update_one(
            {"_id": ObjectId(testimonial_id)}, {"$set": updated_data}
        )

    @staticmethod
    def delete(testimonial_id: str):
        """Delete a testimonial by ID."""
        return TestimonialRepository.collection.delete_one({"_id": ObjectId(testimonial_id)})
