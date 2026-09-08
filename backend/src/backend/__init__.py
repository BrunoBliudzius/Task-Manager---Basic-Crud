from src.backend.api.v1.routes.get import router as search_appointments_router
from src.backend.api.v1.routes.post import router as create_appointments_router
from src.backend.api.v1.routes.delete import router as delete_appointments_router

from src.backend.api.v2.routes.get import router as search_appointments_router2
from src.backend.api.v2.routes.post import router as create_appointments_router2

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    prefix="/api/v1/appointments",
    tags=["appointments v1"],
    router=search_appointments_router,
)
app.include_router(
    prefix="/api/v1/appointments",
    tags=["appointments v1"],
    router=create_appointments_router,
)
app.include_router(
    prefix="/api/v1/appointments",
    tags=["appointments v1"],
    router=delete_appointments_router,
)
app.include_router(
    prefix="/api/v2/appointments",
    tags=["appointments v2"],
    router=search_appointments_router2,
)
app.include_router(
    prefix="/api/v2/appointments",
    tags=["appointments v2"],
    router=create_appointments_router2,
)
