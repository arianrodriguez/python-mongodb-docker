from fastapi import FastAPI
from .routes.user_routes import router as route_users

app = FastAPI(
    title="FastAPI with MongoDB",
    description="This is a simple FastAPI with MongoDB project",
    version="0.1.0",
    openapi_tags=[
        {
            "name": "Users",
            "description": "Operations related to users"
        }
    ],
    redoc_url=None
)#

app.include_router(route_users, prefix="/api/v1")