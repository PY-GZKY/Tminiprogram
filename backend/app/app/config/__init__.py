# -*- coding: utf-8 -*-
import os
from ..logger import logger
from dotenv import load_dotenv
load_dotenv(dotenv_path="/production.env", verbose=True)

p_env_ = os.getenv("PRODUCTION", None)
if p_env_:
    logger.debug("线上环境启动 .... DONE")
    from .production_config import settings
else:
    logger.debug("开发环境启动 .... DONE")
    from .development_config import settings
