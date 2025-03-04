from typing import Union
from pydantic import BaseModel
from fastapi import APIRouter

from .Users import router as users_router
from .Conversations import router as conversations_router
from .Comments import router as comments_router

router = APIRouter(tags=["Database"])
prefix = __name__.split('.')[-2]
prefix = '_'.join(prefix.split('_')[2:])
dependencies = []

router.include_router(users_router)
router.include_router(conversations_router)
router.include_router(comments_router)
