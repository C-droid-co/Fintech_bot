from motor.motor_asyncio import AsyncIOMotorClient as MongoClient

from ftb.config import get_str_key

MONGO2 = get_str_key("MONGO_URL_2", None)
MONGO = get_str_key("MONGO_URL", required=True)
if MONGO2 == None:
    MONGO2 = MONGO

mongo_client = MongoClient(MONGO_URL_2)
db = mongo_client.ftb2
