from pathlib import Path

from ...api import app


@app.get("/")
def read_root():
    return {"Hello": "World"}
