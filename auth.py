from fastapi import APIRouter
from database import ENGINE, session
from models import Users
from fastapi import HTTPException
from fastapi import status
from schemas import RegisterModel, LoginModel
from werkzeug import security

session = session(bind=ENGINE)

auth_router = APIRouter(prefix="/auth")

@auth_router.get("/")
async def auth():
    return {
        "message": "This is auth page"
    }


@auth_router.get("/register")
async def register():
    return {
        "message": "GET request"
    }


@auth_router.post("/register")
async def register(user: RegisterModel):
    username = session.query(Users).filter(Users.username == user.username).first()
    if username is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Bunday username mavjud")

    email = session.query(Users).filter(Users.email == user.email).first()
    if email is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Bunday email mavjud")

    new_user = Users(
        id=user.id,
        first_name=user.first_name,
        last_name=user.last_name,
        username=user.username,
        password=security.generate_password_hash(user.password),
        email=user.email,
        is_staff=user.is_staff,
        is_active=user.is_active
    )

    session.add(new_user)
    session.commit()
    return HTTPException(status_code=status.HTTP_201_CREATED, detail="Successfully")


@auth_router.get("/login")
async def login():
    return {
        "message": "This is login page"
    }


@auth_router.post("/login")
async def login(user: LoginModel):
    username = session.query(Users).filter(Users.username == user.username).first()
    if username is not None:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Username xato")

    user_check = session.query(Users).filter(Users.username == user.username).first()
    if security.check_password_hash(user_check.password, user.password):
        return HTTPException(status_code=status.HTTP_200_OK, detail=f"{user.username} login")

    return HTTPException(detail="username yoki password xato")



@auth_router.get("/logout")
async def logout():
    return {
        "message": "This is logout page"
    }

