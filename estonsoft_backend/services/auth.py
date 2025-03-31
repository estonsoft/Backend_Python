from repositories.user import UserRepository
from lib.bcrypt import verify_password
from lib.jwt import generate_token

class AuthService:
    @staticmethod
    def login(email: str, password: str):
        """Authenticate user and generate JWT token"""
        user = UserRepository.get_user_by_email(email)
        
        if not user or not verify_password(password, user["password"]):
            return None  # Invalid credentials
        token = generate_token(user["email"])
        return {"token": token, "message": "✅ Login successful"}

    @staticmethod
    def get_user_info(user_id: str):
        """Retrieve user info by token"""
        return UserRepository.get_user_by_id(user_id)
