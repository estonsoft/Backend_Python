from fastapi import HTTPException
from models.portfolio import Portfolio
from repositories.portfolio import PortfolioRepository


class PortfolioService:
    
    @staticmethod
    def create_portfolio(portfolio: Portfolio, auth_user: dict):
        if "create_portfolio" not in auth_user.get("permissions", []):
            raise HTTPException(status_code=403, detail="❌ Permission denied")

        portfolio_data = portfolio.model_dump()
        portfolio_data["user_id"] = str(auth_user["_id"])

        inserted_id = PortfolioRepository.create(portfolio_data)
        return {"id": str(inserted_id), "message": "✅ Portfolio created successfully"}

    @staticmethod
    def get_all_portfolios(auth_user: dict):
        if "read_portfolio" not in auth_user.get("permissions", []):
            raise HTTPException(status_code=403, detail="❌ Permission denied")

        portfolios = PortfolioRepository.get_all()
        return [PortfolioService.portfolio_helper(port) for port in portfolios]

    @staticmethod
    def get_portfolio_by_id(portfolio_id: str, auth_user: dict):
        if "read_portfolio" not in auth_user.get("permissions", []):
            raise HTTPException(status_code=403, detail="❌ Permission denied")

        portfolio = PortfolioRepository.get_by_id(portfolio_id)
        if not portfolio:
            raise HTTPException(status_code=404, detail="❌ Portfolio not found")

        return PortfolioService.portfolio_helper(portfolio)

    @staticmethod
    def update_portfolio(portfolio_id: str, updated_portfolio: Portfolio, auth_user: dict):
        if "update_portfolio" not in auth_user.get("permissions", []):
            raise HTTPException(status_code=403, detail="❌ Permission denied")

        existing_portfolio = PortfolioRepository.get_by_id(portfolio_id)
        if not existing_portfolio:
            raise HTTPException(status_code=404, detail="❌ Portfolio not found")

        if str(existing_portfolio["user_id"]) != str(auth_user["_id"]):
            raise HTTPException(status_code=403, detail="❌ You are not authorized to update this portfolio")

        updated_data = updated_portfolio.model_dump(exclude_unset=True)
        updated_data.pop("user_id", None)

        PortfolioRepository.update(portfolio_id, updated_data)
        return {"message": "✅ Portfolio updated successfully"}

    @staticmethod
    def delete_portfolio(portfolio_id: str, auth_user: dict):
        if "delete_portfolio" not in auth_user.get("permissions", []):
            raise HTTPException(status_code=403, detail="❌ Permission denied")

        existing_portfolio = PortfolioRepository.get_by_id(portfolio_id)
        if not existing_portfolio:
            raise HTTPException(status_code=404, detail="❌ Portfolio not found")

        if str(existing_portfolio["user_id"]) != str(auth_user["_id"]):
            raise HTTPException(status_code=403, detail="❌ You are not authorized to delete this portfolio")

        PortfolioRepository.delete(portfolio_id)
        return {"message": "✅ Portfolio deleted successfully"}
    
    @staticmethod
    def portfolio_helper(portfolio) -> dict:
        """Helper function to format portfolio response"""
        return {
            "id": str(portfolio["_id"]),
            "title": portfolio.get("title", ""),
            "description": portfolio.get("description", ""),
            "image": portfolio.get("image", ""),
            "link": portfolio.get("link", "")
        }
