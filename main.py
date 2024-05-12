from fastapi import FastAPI, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from pages.pouter import router
import uvicorn

app = FastAPI(
    title="YourHobby"
)
favicon_path = 'favicon.ico'


templates = Jinja2Templates(directory="templates")


app.include_router(router)

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)

    