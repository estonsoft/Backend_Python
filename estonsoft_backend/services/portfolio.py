from repositories.portfolio import PortfolioRepository

class PortfolioService:
    @staticmethod
    def create_post(portfolio_post: dict):
        return PortfolioRepository.create(portfolio_post)

    @staticmethod
    def get_all_posts():
        return PortfolioRepository.get_all()

    @staticmethod
    def get_post_by_id(post_id: str):
        return PortfolioRepository.get_by_id(post_id)

    @staticmethod
    def update_post(post_id: str, update_data: dict):
        return PortfolioRepository.update(post_id, update_data)

    @staticmethod
    def delete_post(post_id: str):
        return PortfolioRepository.delete(post_id)
