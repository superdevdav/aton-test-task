from database import *
from models import *
from UserRepository import UserRepository
from sqlalchemy.orm import Session
from fastapi import APIRouter, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from pathlib import Path
from utils import hash_password

router = APIRouter()

template_dir = Path(__file__).parent.parent / "templates"
templates = Jinja2Templates(directory=str(template_dir))

# Базовая страница (авторизация)
@router.get("/", response_class=HTMLResponse)
async def userLogin(request: Request, error: str = None):
    return templates.TemplateResponse("auth.html", {"request": request, "error": error})

# Панель управления пользователя
@router.post("/panel")
async def userPanel(request: Request, login: str = Form(None), password: str = Form(None), db: Session = Depends(get_db)):
    if login and password:
        hashed_password = hash_password(password)
        user = db.query(User).filter(User.login == login, User.password == hashed_password).first()
        if user:
            user_full_name = user.full_name.split(" ")
            surname, name, patrynomic = user_full_name[0], user_full_name[1], ""

            # Проверка на то, что есть отчество у пользователя
            if len(user_full_name) == 3:
                patrynomic = user_full_name[2]
            
            request.session["user_id"] = user.id
            request.session["user_name"] = name
            request.session["user_responsible"] = f"{surname} {name} {patrynomic}"
        else:
            return RedirectResponse(url="/?error=true", status_code=303)
    else:
        if "user_id" not in request.session:
            return RedirectResponse(url="/?error=true", status_code=303)
        
    userResponsible = request.session["user_responsible"]
    customers = db.query(Customer).filter(Customer.full_name_responsible == userResponsible)
    return templates.TemplateResponse("user_panel.html", {"request": request, "name": request.session["user_name"], "customers": customers})

# Маршрут для обновления статуса клиента
@router.post("/update_status")
async def updatePanelDataStatus(request: Request, customer_id: int = Form(...), status: str = Form(...), db: Session = Depends(get_db)):
    if "user_id" not in request.session:
        return RedirectResponse(url="/?error=true", status_code=303)
    UserRepository.updateCustomerStatus(customer_id, status, db)
    return RedirectResponse(url="/panel")