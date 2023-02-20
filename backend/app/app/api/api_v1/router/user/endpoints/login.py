# from datetime import timedelta
# from typing import Any
#
# from fastapi import APIRouter, Depends, HTTPException
# from fastapi.security import OAuth2PasswordRequestForm
# from sqlalchemy.orm import Session
#
# from app.api.utils.responseCode import resp_400
# from app.common import deps
# from app.config import settings
# from app.security import security
#
# router = APIRouter()
#
#
# @router.post("/login/token")  # exclude_dependencies=True
# def login_token(db: Session = Depends(deps.get_db), form_data: OAuth2PasswordRequestForm = Depends()) -> Any:
#     """Web Login Api"""
#     # user = user_menu.user.authenticate(db, username=form_data.username, password=form_data.password)
#     # if not user:
#     #     raise HTTPException(status_code=400, detail="Incorrect email or password")
#     # elif not user_menu.user.is_active(user):
#     #     raise HTTPException(status_code=400, detail="Inactive user")
#     # access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
#     # return {
#     #     "code": 20000,
#     #     "data": {
#     #         "token": security.create_access_token(user.id, expires_delta=access_token_expires),
#     #         "token_type": "bearer",
#     #     },
#     #     "message": "",
#     # }
#
#     """ldap Login Api"""
#     user = ldap_authenticate(db, username=form_data.username, password=form_data.password)
#     if not user:
#         return resp_400(message="Incorrect username or password")
#     elif not user_menu.user.is_active(user):
#         return resp_400(message="Inactive user")
#     access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
#     # print(user.role_ids)
#     return {
#         "code": 20000,
#         "data": {
#             "token": security.create_access_token(user.id, expires_delta=access_token_expires),
#             "token_type": "bearer",
#             "nickname": user.nickname,
#             "roles": {
#                 "is_check": True if 1000007 in user.role_ids else False,
#                 "is_dev": True if 1000010 in user.role_ids else False
#             },
#
#         },
#         "message": "",
#     }
#
#
# @router.post("/login/access-token", )  # exclude_dependencies=True
# def login_access_token(db: Session = Depends(deps.get_db), form_data: OAuth2PasswordRequestForm = Depends()) -> Any:
#     """OAuth2 compatible token login, get an access token for future requests"""
#     user = user_menu.user.authenticate(db, username=form_data.username, password=form_data.password)
#     if not user:
#         raise HTTPException(status_code=400, detail="Incorrect email or password")
#     elif not user_menu.user.is_active(user):
#         raise HTTPException(status_code=400, detail="Inactive user")
#     access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
#     return {
#         "access_token": security.create_access_token(user.id, expires_delta=access_token_expires),
#         "token_type": "bearer",
#     }
#
#
# @router.post("/logout")
# def logout() -> Any:
#     """logout"""
#     return {"code": 20000, "data": {"logout": True}, "message": "", }
