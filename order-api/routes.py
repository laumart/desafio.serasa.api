from fastapi import APIRouter
from controllers import order_controller

api_router = APIRouter()
api_router.include_router(order_controller.router, tags=["orders"])
