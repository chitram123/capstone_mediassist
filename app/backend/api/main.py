from fastapi import FastAPI

from app.backend.api.health_api import router as health_router
from app.backend.api.upload_api import router as upload_router
from app.backend.api.retrieval_api import router as retrieve_router
from app.backend.api.chat_api import router as chat_router
from app.backend.api.image_api import router as image_router


app = FastAPI(
    title="MediAssist AI"
)

app.include_router(health_router)
app.include_router(upload_router)
app.include_router(retrieve_router)
app.include_router(chat_router)
app.include_router(image_router)