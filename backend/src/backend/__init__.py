from fastapi import FastAPI
from src.backend.api.routes.get import router as search_appointments_router
from src.backend.api.routes.post import router as create_appointments_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(search_appointments_router)
app.include_router(create_appointments_router)
