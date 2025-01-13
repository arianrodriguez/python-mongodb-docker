from ..repositories.user_repository import UserRepository
from ..models.user_model import UserModel

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def create_user(self, user: UserModel) -> str:
        return await self.repository.create_user(user)