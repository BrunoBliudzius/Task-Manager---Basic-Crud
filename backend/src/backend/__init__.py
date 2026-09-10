from src.backend.api.v1.routes.get import router as search_appointments_router
from src.backend.api.v1.routes.post import router as create_appointments_router
from src.backend.api.v1.routes.delete import router as delete_appointments_router
from src.backend.api.v1.routes.update import router as update_appointments_router

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import os
from dotenv import load_dotenv

load_dotenv()

is_production = os.getenv("ENVIRONMENT") == "production"

app = FastAPI(
    docs_url=None if is_production else "/docs",
    redoc_url=None if is_production else "/redoc",
    openapi_url=None if is_production else "/openapi.json",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://taskmanager-bice-sigma.vercel.app"],
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
    prefix="/api/v1/appointments",
    tags=["appointments v1"],
    router=update_appointments_router,
)
