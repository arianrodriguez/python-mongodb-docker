from fastapi import APIRouter, HTTPException, Depends
from http import HTTPStatus
from fastapi.responses import JSONResponse
from ..models.user_model import UserModel
from ..dependencies.user_dependency import get_user_service
from ..services.user_service import UserService

router = APIRouter()

@router.post("/users", tags=["Users"], response_description="Add new user")
async def add_new_user(user: UserModel, service: UserService = Depends(get_user_service)) -> JSONResponse:
    try:
        user_id = await service.create_user(user)

        return JSONResponse(
            status_code=HTTPStatus.CREATED, 
            content={
                "id": user_id,
                "message": "User created successfully"
            }
        )
    except ValueError as e:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail=str(e)
        )