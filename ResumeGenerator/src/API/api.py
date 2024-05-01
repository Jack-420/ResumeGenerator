from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .routes import base, data, resume

app = FastAPI()
app.include_router(base.router)
app.include_router(data.router)
app.include_router(resume.router)

app.mount(
    "/static",
    StaticFiles(directory="ResumeGenerator/src/API/routes/static"),
    name="static",
)
