from fastapi import APIRouter
from pydantic import BaseModel

from common.config import BusinessException
from common.utils.ResponseRes import R

from enity.dto.request_user import UserRegisterRequest
from models.user import User
from jwt.exceptions import InvalidTokenError
user_router = APIRouter(prefix="/user", tags=["用户管理"])


@user_router.get("/list", summary="获取用户列表")
async def get_users():
    return R.ok(data=await User.all())


@user_router.post("/register", summary="注册用户")
async def register_user(body: UserRegisterRequest|None):
    if body is None:
        raise BusinessException(400, "参数不能为空")
    userAccount = body.userAccount
    userPassword = body.userPassword
    checkPassword = body.checkPassword
    if userPassword != checkPassword:
        raise BusinessException(400, "两次密码不一致")
    user = await User.filter(userAccount=userAccount).first()
    if user:
        raise BusinessException(400, "用户已存在")
    await User.create(userAccount=userAccount, userPassword=userPassword)
    return R.ok(msg="注册成功")
@user_router.post("/login", summary="登录")
async def login_user():
    return R.ok(msg="登录成功")


