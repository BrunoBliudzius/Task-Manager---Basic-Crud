from src.backend.api.routes.post import appointment_list
from fastapi import APIRouter

router = APIRouter(prefix="/appointments", tags=["appointments"])


@router.get("/")
async def get_appointments():
    return appointment_list
