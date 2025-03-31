from fastapi import APIRouter, Depends, HTTPException
from typing import List
from models.portfolio import Portfolio, PortfolioResponse
from services.portfolio import PortfolioService
from lib.jwt import verify_token

router = APIRouter(prefix="/portfolios")

@router.post("/", response_model=dict)
async def create_portfolio(portfolio: Portfolio, auth_user: dict = Depends(verify_token)):
    return PortfolioService.create_portfolio(portfolio, auth_user)

@router.get("/", response_model=List[PortfolioResponse])
async def get_all_portfolios(auth_user: dict = Depends(verify_token)):
    return PortfolioService.get_all_portfolios(auth_user)

@router.get("/{portfolio_id}", response_model=PortfolioResponse)
async def get_portfolio(portfolio_id: str, auth_user: dict = Depends(verify_token)):
    return PortfolioService.get_portfolio_by_id(portfolio_id, auth_user)

@router.put("/{portfolio_id}", response_model=dict)
async def update_portfolio(portfolio_id: str, updated_portfolio: Portfolio, auth_user: dict = Depends(verify_token)):
    return PortfolioService.update_portfolio(portfolio_id, updated_portfolio, auth_user)

@router.delete("/{portfolio_id}", response_model=dict)
async def delete_portfolio(portfolio_id: str, auth_user: dict = Depends(verify_token)):
    return PortfolioService.delete_portfolio(portfolio_id, auth_user)
