from motor.motor_asyncio import AsyncIOMotorDatabase
from ..models.user_model import UserModel

class UserRepository:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.collection = db.get_collection("users")

    async def create_user(self, user: UserModel) -> str:
        result = await self.collection.insert_one(user.dict())
        return str(result.inserted_id)