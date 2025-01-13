from ..config.database import connection
from ..repositories.user_repository import UserRepository
from ..services.user_service import UserService

def get_user_service() -> UserService:
    db = connection.get_db("test-python")
    repository = UserRepository(db)
    return UserService(repository)