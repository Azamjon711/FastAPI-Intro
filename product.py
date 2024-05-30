from fastapi import APIRouter, HTTPException, status
from models import Product, Category
from schemas import ProductModel
from fastapi.encoders import jsonable_encoder
from database import session, ENGINE

session = session(bind=ENGINE)

product_router = APIRouter(prefix="/product")


@product_router.get("/")
async def product_list():
    products = session.query(Product).all()
    context = [
        {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "category_id": product.category_id,
        }
        for product in products
    ]

    return jsonable_encoder(context)

@product_router.post("/create")
async def create(product: ProductModel):
    check_product = session.query(Product).filter(Product.id == product.id).first()
    check_category_id = session.query(Category).filter(Category.id == product.category_id).first()

    if check_product:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Already exist")
    elif check_category_id:
        new_product = Product(
            id=product.id,
            name=product.name,
            description=product.description,
            price=product.price,
            category_id=product.category_id,
        )
        session.add(new_product)
        session.commit()
        data = {
            "code": 201,
            "msg": "successful"
        }
        return jsonable_encoder(data)

    return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="category_id already exist")

