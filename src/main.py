from pathlib import Path
from database import *
from models import Base
from sqlalchemy.orm import Session
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from router import router
from UserRepository import UserRepository
from CustomerRepository import CustomerRepository
from starlette.middleware.sessions import SessionMiddleware
import uvicorn

Base.metadata.create_all(bind=engine)

app = FastAPI(title="ATON App")

app.add_middleware(SessionMiddleware, secret_key="your-secret-key")

app.include_router(router)

# Функция для создания синтетических пользователей и клиентов
def create_synthetic_data():
    with Session(engine) as db:
        user_result = UserRepository.createSyntheticUsers(db)
        print(user_result)
        customer_result = CustomerRepository.createSyntheticCustomers(db)
        print(customer_result)

# Вызов функции для создания синтетических данных
create_synthetic_data()

static_dir = Path(__file__).resolve().parent.parent / "static"
app.mount("/static", StaticFiles(directory=static_dir), name="static")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)