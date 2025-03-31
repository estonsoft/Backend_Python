from fastapi import HTTPException
from models.testimonials import Testimonial
from repositories.testimonials import TestimonialRepository


class TestimonialService:

    @staticmethod
    def create_testimonial(testimonial: Testimonial, auth_user: dict):
        if "create_testimonial" not in auth_user.get("permissions", []):
            raise HTTPException(status_code=403, detail="❌ Permission denied")

        testimonial_data = testimonial.model_dump()
        testimonial_data["user_id"] = str(auth_user["_id"])

        inserted_id = TestimonialRepository.create(testimonial_data)
        return {"id": str(inserted_id), "message": "✅ Testimonial created successfully"}

    @staticmethod
    def get_all_testimonials(auth_user: dict):
        if "read_testimonial" not in auth_user.get("permissions", []):
            raise HTTPException(status_code=403, detail="❌ Permission denied")

        testimonials = TestimonialRepository.get_all()
        return [TestimonialService.testimonial_helper(test) for test in testimonials]

    @staticmethod
    def get_testimonial_by_id(testimonial_id: str, auth_user: dict):
        if "read_testimonial" not in auth_user.get("permissions", []):
            raise HTTPException(status_code=403, detail="❌ Permission denied")

        testimonial = TestimonialRepository.get_by_id(testimonial_id)
        if not testimonial:
            raise HTTPException(status_code=404, detail="❌ Testimonial not found")

        return TestimonialService.testimonial_helper(testimonial)

    @staticmethod
    def update_testimonial(testimonial_id: str, updated_testimonial: Testimonial, auth_user: dict):
        if "update_testimonial" not in auth_user.get("permissions", []):
            raise HTTPException(status_code=403, detail="❌ Permission denied")

        existing_testimonial = TestimonialRepository.get_by_id(testimonial_id)
        if not existing_testimonial:
            raise HTTPException(status_code=404, detail="❌ Testimonial not found")

        if str(existing_testimonial["user_id"]) != str(auth_user["_id"]):
            raise HTTPException(status_code=403, detail="❌ You are not authorized to update this testimonial")

        updated_data = updated_testimonial.model_dump(exclude_unset=True)
        updated_data.pop("user_id", None)

        TestimonialRepository.update(testimonial_id, updated_data)
        return {"message": "✅ Testimonial updated successfully"}

    @staticmethod
    def delete_testimonial(testimonial_id: str, auth_user: dict):
        if "delete_testimonial" not in auth_user.get("permissions", []):
            raise HTTPException(status_code=403, detail="❌ Permission denied")

        existing_testimonial = TestimonialRepository.get_by_id(testimonial_id)
        if not existing_testimonial:
            raise HTTPException(status_code=404, detail="❌ Testimonial not found")

        if str(existing_testimonial["user_id"]) != str(auth_user["_id"]):
            raise HTTPException(status_code=403, detail="❌ You are not authorized to delete this testimonial")

        TestimonialRepository.delete(testimonial_id)
        return {"message": "✅ Testimonial deleted successfully"}

    @staticmethod
    def testimonial_helper(testimonial) -> dict:
        """Helper function to format testimonial response"""
        return {
            "id": str(testimonial["_id"]),
            "star": testimonial["star"],
            "name": testimonial["name"],
            "image": testimonial["image"],
            "content": testimonial["content"],
            "designation": testimonial["designation"]
        }