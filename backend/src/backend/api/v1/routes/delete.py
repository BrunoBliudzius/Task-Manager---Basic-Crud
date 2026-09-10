from typing import Annotated
from fastapi import APIRouter, Path, Response, status, Depends
from src.backend.api.con import get_connection

router = APIRouter()


@router.delete("/{id}")
async def delete_appointment(
    id: Annotated[int, Path(gt=0)],
    connection=Depends(get_connection),
):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM public.appointments WHERE id = %s;", (id,))
        connection.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
