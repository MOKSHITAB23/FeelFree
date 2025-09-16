from db import logintab

async def signup(creds:dict):
    query = await logintab.find_one({"username":creds["username"]})
    if query:
        return {"error":"Username already exists"}
    else:
        result = await logintab.insert_one(creds)
        query = await logintab.find_one({"_id":result.inserted_id})
        return query
        