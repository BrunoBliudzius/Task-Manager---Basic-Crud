from pydantic import BaseModel, Field
from fastapi import APIRouter, Body
from typing import Annotated
from datetime import date

router = APIRouter()


class Appointment(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    description: str = Field(max_length=200)
    date: date
    end_time: date


appointment_list: list[Appointment] = []


@router.post("/")
async def create_appointment(appointment: Annotated[Appointment, Body()]):
    appointment_list.append(appointment)
    return {"message": "Appointment created successfully"}
