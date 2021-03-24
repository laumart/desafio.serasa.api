from schema.order_schema import Order, OrderUpdate
from models.order import OrderBase
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


router = APIRouter()

# Listar, exibir, criar, alterar e excluir pedidos


@router.get("/api/order/{order_id}")
async def get_order(order_id: str):
    order = OrderBase()
    return order.select_order(order_id)


@router.get("/api/order/user/{user_id}")
async def get_order_by_user(user_id):
    order = OrderBase()
    return order.select_order_by_user(user_id)


@router.get("/api/orders")
async def get_orders():
    order = OrderBase()
    return order.select_allorders()


@router.post("/api/order", include_in_schema=True, summary="Create Order", status_code=201)
async def save_order(order: Order):
    order_include = OrderBase()
    return order_include.save_order(order)


@router.put("/api/order/{order_id}")
async def update_order(order_id: str, order: OrderUpdate):
    order_up = OrderBase()
    json_converte = jsonable_encoder(order_up.update_order(order_id, order))
    return JSONResponse(content=json_converte)


@router.delete("/api/order/{order_id}")
async def delete_order(order_id: str):
    order_del = OrderBase()
    return order_del.delete_order(order_id)







