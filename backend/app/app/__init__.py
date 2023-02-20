# -*- coding: utf-8 -*-
import os
import sys

from starlette.middleware.cors import CORSMiddleware

from app.db.mongo_db import db
from app.logger import logger

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from fastapi import FastAPI

from app.config import settings
from app.api.api_v1.api import api_v1_router


def create_app():
    app = FastAPI(
        debug=settings.DEBUG,
        title=settings.PROJECT_NAME,  # 项目名称
        description=settings.DESCRIPTION,  # 项目简介
        docs_url=f"{settings.API_V1_STR}/docs",  # 自定义 docs文档的访问路径
        openapi_url=f"{settings.API_V1_STR}/openapi.json"
        # docs_url=None,  # 禁用文档
        # openapi_url=None
    )

    # 注册mongodb
    # register_mongodb(app)

    # 跨域设置
    register_cors(app)

    # 注册路由
    register_router(app)

    return app


def register_mysql(app: FastAPI):
    @app.on_event("startup")
    async def connect_to_mysql():
        logger.debug("MYSQL 数据库初始化成功 ... DONE")


# def register_mongodb(app: FastAPI):
#     @app.on_event("startup")
#     async def connect_to_mongo():
#         try:
#             db.client = MongoClient(settings.MONGODB_URL, maxPoolSize=settings.MAX_CONNECTIONS_COUNT,
#                                     minPoolSize=settings.MIN_CONNECTIONS_COUNT)
#
#             logger.debug("MONGODB 数据库初始化成功 ... DONE")
#         except Exception:
#             logger.error("MONGODB 数据库初始化失败 ... DONE")
#
#     @app.on_event("shutdown")
#     async def close_mongo_connection():
#         logger.debug("MONGODB 数据库连接关闭 ... DONE")


def register_cors(app: FastAPI):
    """
    支持跨域
    :param app:
    :return:
    """
    if settings.BACKEND_CORS_ORIGINS:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=settings.BACKEND_CORS_ORIGINS,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )


def register_router(app: FastAPI):
    """
    :param app:
    :return:
    """
    app.include_router(
        api_v1_router,
        # prefix=settings.API_V1_STR  # 前缀
    )
