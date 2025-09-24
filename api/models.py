from pydantic import BaseModel

class userCreate(BaseModel):
    username: str
    password: str

class userOut(BaseModel):
    id:str
    username: str

class Message(BaseModel):
    message:str

class MessageOut(BaseModel):
    message:str