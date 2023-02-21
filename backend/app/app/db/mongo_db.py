# -*- coding: utf-8 -*

from pymongo import MongoClient


class DataBase:
    client: MongoClient = None


db = DataBase()


async def get_mongo_() -> MongoClient:
    return db.client

# mongo_c_ = MongoClient(host=settings.MONGO_HOST, port=settings.MONGO_PORT, username=settings.MONGO_USER, password=settings.MONGO_PASS)
