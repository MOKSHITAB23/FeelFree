from fastapi import FastAPI
from main import chat
from auth import signup
from models import userCreate,userOut, Message,MessageOut
from fastapi.middleware.cors import CORSMiddleware

server = FastAPI()
# Allow frontend origins
origins = [
    "*"  # allow all (not safe for production, but good for testing)
]

server.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # allowed origins
    allow_credentials=True,
    allow_methods=["*"],         # allow all methods including OPTIONS
    allow_headers=["*"],         # allow all headers
)
@server.post("/chat") # decorator
def func(msg : Message):

    response=chat(msg.model_dump()["message"])
    return MessageOut(message=response)

@server.post("/signup")
async def signUp(user:userCreate):
    data=user.model_dump()
    response=await signup(data)
    if "error" in response:
        return response
    resp = userOut(username=response["username"],id=str(response["_id"]))
    return resp
