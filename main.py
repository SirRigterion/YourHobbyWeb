from fastapi import FastAPI
from pages.router import router as router_pages
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="YourHobby"
)

app.include_router(router_pages)


app.mount("/static", StaticFiles(directory="static"), name="ststic")