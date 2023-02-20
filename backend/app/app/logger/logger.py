# -*- coding: utf-8 -*-
import time
from loguru import logger

# 测试环境不存入 .log 文件
# logger.start(f'log/{time.strftime("%Y-%m-%d", time.localtime())}.log',
#              format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}", encoding='utf-8')

