from typing import Annotated
from fastapi import APIRouter, Path, Depends, Response, Body,status
from src.backend.api.con import get_connection
from src.backend.api.v1.routes.post import Appointment

router = APIRouter()


@router.put("/{id}")
async def update_appointment(
    id: Annotated[int, Path(gt=0)],
    appointment: Annotated[Appointment, Body()],
    connection=Depends(get_connection),
):
    with connection.cursor() as cursor:
        cursor.execute(
            "UPDATE public.appointments SET title = %s, description = %s, date = %s, end_time = %s WHERE id = %s;",
            (
                appointment.title,
                appointment.description,
                appointment.date,
                appointment.end_time,
                id,
            ),
        )
        connection.commit()
    return Response(status_code=status.HTTP_200_OK)
