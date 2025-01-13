from motor.motor_asyncio import AsyncIOMotorDatabase
from ..models.user_model import UserModel

class UserRepository:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.collection = db.get_collection("users")

    async def create_user(self, user: UserModel) -> str | None:
        try:
            result = await self.collection.insert_one(user.dict())
            return str(result.inserted_id)
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    async def get_user_by_username(self, username: str) -> UserModel | None:
        try:
            user = await self.collection.find_one({
                "username": username
            })
            if not user: raise ValueError(f"User with username {username} not found")
            return UserModel(**user)
        except Exception as e:  
            print(f"Error: {e}")
            return None