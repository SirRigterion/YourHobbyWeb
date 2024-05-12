from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(
    tags=["Страницы"]
)

templates = Jinja2Templates(directory="templates")

@router.get("/")
async def get_main_page(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})

@router.get("/base")
async def get_base_page(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})

@router.get("/main")
async def get_main_page(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})

@router.get("/creation")
async def get_art_page(request: Request):
    return templates.TemplateResponse("creation.html", {"request": request})

@router.get("/science")
async def get_science_page(request: Request):
    return templates.TemplateResponse("science.html", {"request": request})

@router.get("/sport")
async def get_sport_page(request: Request):
    return templates.TemplateResponse("sport.html", {"request": request})

@router.get("/computer")
async def get_computer_page(request: Request):
    return templates.TemplateResponse("computer.html", {"request": request})

@router.get("/reading")
async def get_reading_page(request: Request):
    return templates.TemplateResponse("reading.html", {"request": request})

@router.get("/collecting")
async def get_collecting_page(request: Request):
    return templates.TemplateResponse("collecting.html", {"request": request})

@router.get("/studying")
async def get_studying_page(request: Request):
    return templates.TemplateResponse("studying.html", {"request": request})
