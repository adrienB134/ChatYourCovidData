import uvicorn

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI


from routes import routes

import os


app = FastAPI(
    title="Chat Your Data",
)

app.include_router(routes.router)
app.mount("/static", StaticFiles(directory="./static"), name="static")
app.mount("/cache", StaticFiles(directory="./cache"), name="cache")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=4000)
