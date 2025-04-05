from fastapi import APIRouter, Depends, HTTPException

from typing import List

router = APIRouter()

@router.get("/", response_model=dict)
def health_check1():
    return {"status": "this is Estonsoft backend"}

@router.get("/health", response_model=dict)
def health_check():
    return {"status": "this is health checks"}


