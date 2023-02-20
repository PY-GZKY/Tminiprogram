# -*- coding: utf-8 -*-

class UserTokenError(Exception):
    def __init__(self, err_desc: str = "用户认证异常"):
        self.err_desc = err_desc


class UserNotFound(Exception):
    def __init__(self, err_desc: str = "没有此用户", ):
        self.err_desc = err_desc


class PostParamsError(Exception):
    def __init__(self, err_desc: str = "POST请求参数错误"):
        self.err_desc = err_desc
