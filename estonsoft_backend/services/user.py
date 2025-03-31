from repositories.user import UserRepository
from lib.bcrypt import hash_password
from lib.jwt import generate_token
import os

class UserService:
    @staticmethod
    def create_user(user_data: dict):
        # Hash password
        user_data["password"] = hash_password(user_data["password"])
        # Generate token (Optional)
        token = generate_token(user_data["email"])
        # Save user to database
        user_id = UserRepository.create_user(user_data)
        return {"id": user_id, "permissions": user_data["permissions"], "token": token}

    @staticmethod
    def get_all_users():
        return UserRepository.get_all_users()

    @staticmethod
    def get_user_by_id(user_id: str):
        return UserRepository.get_user_by_id(user_id)

    @staticmethod
    def get_user_by_email(email: str):
        return UserRepository.get_user_by_email(email)

    @staticmethod
    def update_user(user_id: str, update_data: dict):
        update_data["password"] = hash_password(update_data["password"])
        return UserRepository.update_user(user_id, update_data)

    @staticmethod
    def delete_user(user_id: str):
        return UserRepository.delete_user(user_id)

    @staticmethod
    def initialize_admin():
        """Create admin user if not exists"""
        adminPassword=os.getenv("ADMIN_PASSWORD")
        if not UserRepository.get_user_by_email("admin@email.com"):
            admin_data = {
                "name": "Admin",
                "email": "admin@email.com",
                "password": hash_password(adminPassword),
                "permissions": [
                    "create_user", "delete_user", "update_user", "view_users",
                    "create_blog", "update_blog", "delete_blog", "read_blog",
                    "create_portfolio", "update_portfolio", "delete_portfolio", "read_portfolio",
                    "create_testimonial", "update_testimonial", "delete_testimonial", "read_testimonial"
                ]
            }
            UserRepository.create_user(admin_data)
            print("✅ Admin user created!")
        else:
            print("ℹ️ Admin user already exists.")