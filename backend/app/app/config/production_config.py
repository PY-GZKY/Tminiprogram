#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import os
import os
from typing import List, Union

from pydantic import AnyHttpUrl, BaseSettings, EmailStr, validator


class Settings(BaseSettings):
    DEBUG = os.getenv("DEBUG", 0)
    PROFILER_ON: bool = 0
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "(-ASp+_)-YRzRE"

    # token过期时间 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    # 根路径
    BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 项目信息
    PROJECT_NAME: str = "LabelTrainingAdmin"
    DESCRIPTION: str = "LabelTrainingAdmin"
    SERVER_NAME: str = "API_V1"

    # 跨域
    BACKEND_CORS_ORIGINS: List[str] = ['*']

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    # MongoDB 配置项
    MAX_CONNECTIONS_COUNT = int(os.getenv("MAX_CONNECTIONS_COUNT", 10))
    MIN_CONNECTIONS_COUNT = int(os.getenv("MIN_CONNECTIONS_COUNT", 1))
    MONGO_HOST: str = os.getenv("MONGO_HOST", "112.74.111.80")
    MONGO_PORT: int = os.getenv("MONGO_PORT", 27017)
    MONGO_USER: str = os.getenv("MONGO_USER", "admin")
    MONGO_PASS: str = os.getenv("MONGO_PASS", ".*?ok123")
    MONGO_DB: str = os.getenv("MONGO_DB", "Tminiprogram")
    MONGODB_URL: str = f"mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:{MONGO_PORT}"

    FIRST_SUPERUSER: str = os.getenv("FIRST_SUPERUSER", None)
    FIRST_MALL: EmailStr = os.getenv("FIRST_MALL", None)
    INIT_SUPERUSER_PASSWORD: str = os.getenv("INIT_SUPERUSER_PASSWORD", None)
    FIRST_ROLE: int = os.getenv("FIRST_ROLE", None)
    FIRST_AVATAR: AnyHttpUrl = os.getenv("FIRST_AVATAR", None)

    class Config:
        case_sensitive = True


# 单例模式的最简写法
settings = Settings()
