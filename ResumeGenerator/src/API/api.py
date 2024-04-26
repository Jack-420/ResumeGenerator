from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .base import router as base_router
from .data import router as data_router
from .resume import router as resume_router

app = FastAPI()
app.include_router(base_router)
app.include_router(data_router)
app.include_router(resume_router)

app.mount(
    "/static", StaticFiles(directory="ResumeGenerator/src/API/static"), name="static"
)
