import logging
from fastapi.exceptions import RequestValidationError
from fastapi import FastAPI, Depends, HTTPException
from flask import Request
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from tortoise.contrib.fastapi import register_tortoise

from common.config import TORTOISE_ORM, BusinessException
from router.user import user_router

app = FastAPI(title="mini-rbac")

register_tortoise(app, config=TORTOISE_ORM)

app.include_router(user_router)
from common.utils.ResponseRes import R
## 自定义异常




@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    logging.error("参数错误", exc_info=exc)
    return R.error(code = 500, msg = "参数错误")

@app.exception_handler(BusinessException)
async def handle_business_exception(request, exc: BusinessException):
    logging.error("BusinessException", exc_info=exc)
    return R.error(exc.code, exc.message)

@app.exception_handler(HTTPException)
async def generic_exception_handler(request: Request, exc: Exception):
    logging.error("Exception", exc_info=exc)
    return R.error(code=200)


# 中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  # 一个允许跨域请求的 HTTP 方法列表
    allow_headers=["*"],  # 一个允许跨域请求的 HTTP 请求头列表
)

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
