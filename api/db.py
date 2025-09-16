from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL="mongodb://localhost:27017/ff"
client = AsyncIOMotorClient(MONGO_URL)

db = client.feelfreedb

logintab = db.logincreds
mood_table = db.moodupdates 