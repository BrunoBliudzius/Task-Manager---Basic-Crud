from src.backend.api.v1.routes.post import appointment_list
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_appointments():
    return appointment_list
