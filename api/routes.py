from fastapi import FastAPI
from main import chat
from auth import signup
from models import userCreate,userOut

server = FastAPI()

@server.post("/chat") # decorator
def func(usr:str):
    response,messages=chat(usr)
    return {"message":response,"messages":messages}

@server.post("/signup")
async def signUp(user:userCreate):
    data=user.model_dump()
    response=await signup(data)
    if "error" in response:
        return response
    resp = userOut(username=response["username"],id=str(response["_id"]))
    return resp
