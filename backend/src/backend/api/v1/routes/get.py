from fastapi import APIRouter, Depends, Path
from typing import Annotated
from src.backend.api.con import get_connection

router = APIRouter()


@router.get("/")
async def get_appointments(
    connection=Depends(get_connection),
):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM public.appointments;")
        appointment_list = cursor.fetchall()
    return appointment_list


@router.get("/{event}")
async def get_appointments_title(
    event: Annotated[str, Path(min_length=1)],
    connection=Depends(get_connection),
):
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM public.appointments where title LIKE %s;", (f"%{event}%",)
        )
        appointment_list = cursor.fetchall()
    return appointment_list
