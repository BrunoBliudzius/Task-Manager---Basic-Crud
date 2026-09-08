from src.backend.api.v1.routes.post import appointment_list
from typing import Annotated
from fastapi import APIRouter, Path, Response, status

router = APIRouter()


@router.delete("/{id}")
async def delete_appointment(id: Annotated[int, Path(gt=0)]):
    appointment_list.pop(id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
