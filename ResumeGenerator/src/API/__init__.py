from fastapi import FastAPI

from .routes import base, data, resume

app = FastAPI()
app.include_router(base.router)
app.include_router(data.router)
app.include_router(resume.router)
