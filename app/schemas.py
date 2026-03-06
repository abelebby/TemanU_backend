from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    name: str
    preferred_name: str
    username: str
    password_hash: str   # not doing auth yet c