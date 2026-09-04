from pydantic import BaseModel, Field
from fastapi import APIRouter, Body
from typing import Annotated
from datetime import date

router = APIRouter(prefix="/appointments", tags=["appointments"])


class Appointment(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    description: str = Field(max_length=200)
    date: date
    end_time: date


class OutputAppointment(Appointment):
    id: int


appointment_list: list[OutputAppointment] = []


@router.post("/")
async def create_appointment(appointment: Annotated[Appointment, Body()]):
    output = OutputAppointment(id=len(appointment_list) + 1, **appointment.model_dump())
    appointment_list.append(output)
    return {"message": "Appointment created successfully"}
