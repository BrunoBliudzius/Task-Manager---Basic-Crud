from pydantic import BaseModel, Field
from fastapi import APIRouter, Body, Depends
from typing import Annotated
from datetime import date
from src.backend.api.con import get_connection

router = APIRouter()


class Appointment(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    description: str = Field(max_length=200)
    date: date
    end_time: date


@router.post("/")
async def create_appointment(
    appointment: Annotated[Appointment, Body()],
    connection=Depends(get_connection),
):
    with connection.cursor() as cursor:
        cursor.execute(
            """
            INSERT INTO public.appointments (title, description, date, end_time)
            VALUES (%s, %s, %s, %s);
            """,
            (
                appointment.title,
                appointment.description,
                appointment.date,
                appointment.end_time,
            ),
        )
        connection.commit()
    return {"message": "Appointment created successfully"}
