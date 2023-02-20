# -*- coding: utf-8 -*
from typing import Generator

from app.config import settings

from pymongo import MongoClient


class DataBase:
    client: MongoClient = None


db = DataBase()


async def get_mongo_database() -> MongoClient:
    return db.client


mongo_c_ = MongoClient(host=settings.MONGO_HOST, port=settings.MONGO_PORT, username=settings.MONGO_USER,
                 password=settings.MONGO_PASS)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        try:
            db.commit()
        except exc.SQLAlchemyError:
            db.rollback()
            print("ERROR DB COMMIT")
        db.close()