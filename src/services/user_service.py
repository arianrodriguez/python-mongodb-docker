from ..repositories.user_repository import UserRepository
from ..models.user_model import UserModel

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def create_user(self, user: UserModel) -> str:
        possible_user = await self.repository.get_user_by_username(user.username)
        if possible_user:
            raise ValueError(f"User with username {user.username} already exists")

        return await self.repository.create_user(user)