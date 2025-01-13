from pydantic import BaseModel

class UserModel(BaseModel):
    username: str
    email: str
    full_name: str
    age: int