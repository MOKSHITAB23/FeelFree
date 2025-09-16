from pydantic import BaseModel

class userCreate(BaseModel):
    username: str
    password: str

class userOut(BaseModel):
    id:str
    username: str
