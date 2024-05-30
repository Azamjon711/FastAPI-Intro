from models import Orders, Users, Product
from schemas import OrderModel
from fastapi import APIRouter, HTTPException, status
from fastapi.encoders import jsonable_encoder
from database import session, ENGINE

session = session(bind=ENGINE)

order_router = APIRouter(prefix="/order")

@order_router.get("/")
async def orders_list():
    orders = session.query(Orders).all()
    context = [
        {
            "id": order.id,
            "user_id": order.users_id,
            "product_id": order.product_id,
        }
        for order in orders
    ]

    return jsonable_encoder(context)


@order_router.post("/create")
async def create(order: OrderModel):
    check_order = session.query(Orders).filter(Orders.id == order.id).first()
    check_user_id = session.query(Users).filter(Users.id == order.users_id).first()
    check_product_id = session.query(Product).filter(Product.id == order.product_id).first()

    if check_order:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Allready exist")
    elif check_user_id and check_product_id:
        new_order = Orders(
            id=order.id,
            user_id=order.users_id,
            product_id=order.product_id
        )
        session.add(new_order)
        session.commit()
        data = {
            "code": 201,
            "msg": "successfull"
        }
        return jsonable_encoder(data)

    return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=" user_id or product_id is allready exist")

