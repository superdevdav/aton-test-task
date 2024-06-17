from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Date

class Base(DeclarativeBase):
     pass

class User(Base):
    __tablename__ = "users"
 
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    full_name: Mapped[str] = mapped_column(String)
    login: Mapped[str] = mapped_column(String, unique=True)
    password: Mapped[str] = mapped_column(String)

class Customer(Base):
     __tablename__ = "customers"
     id: Mapped[int] =  mapped_column(Integer, primary_key=True, index=True)
     account_number: Mapped[int] = mapped_column(Integer)
     surname: Mapped[str] = mapped_column(String)
     name: Mapped[str] = mapped_column(String)
     patrynomic: Mapped[str] = mapped_column(String)
     birth_date: Mapped[Date] = mapped_column(Date)
     inn: Mapped[int] = mapped_column(Integer, unique=True)
     full_name_responsible: Mapped[str] = mapped_column(String)
     status: Mapped[str] = mapped_column(String, default="Не в работе")