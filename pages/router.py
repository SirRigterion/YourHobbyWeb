from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from starlette.responses import FileResponse

router = APIRouter(
    tags=["Pages"]
)

templates = Jinja2Templates(directory="templates")



@router.get("/")
def get_main_page(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})

@router.get("/base")
def get_base_page(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})

@router.get("/main")
def get_main_page(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})

@router.get("/art")
def get_j_page(request: Request):
    return templates.TemplateResponse("art.html", {"request": request})

@router.get("/science")
def get_j_page(request: Request):
    return templates.TemplateResponse("science.html", {"request": request})

@router.get("/sport")
def get_j_page(request: Request):
    return templates.TemplateResponse("sport.html", {"request": request})

@router.get("/computer")
def get_j_page(request: Request):
    return templates.TemplateResponse("computer.html", {"request": request})
