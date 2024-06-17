from sqlalchemy.orm import Session
from sqlalchemy.future import select
from utils import hash_password
from models import *


class UserRepository:
      @classmethod
      def updateCustomerStatus(cls, customer_id, status, db: Session):
            customer = db.query(Customer).filter(Customer.id == customer_id).first()
            if customer:
                  customer.status = status
                  db.commit()
      
      @staticmethod
      def createSyntheticUsers(db: Session):
            try:
                  testSurnames = ['Иванов', 'Орлова', 'Горбушкин']
                  testNames = ['Иван', 'Анна', 'Игорь']
                  testPatrynomics = ['Петрович', 'Олеговна', 'Александрович']
                  testLogins = ['ivan@mail.ru', 'ann@mail.ru', 'igor@mail.ru']
                  testPasswords = [hash_password('ivan123'), hash_password('ann123'), hash_password('igor123')]

                  for i in range(len(testSurnames)):
                        # Проверяем, существует ли пользователь с таким логином
                        existing_user = db.execute(select(User).filter_by(login=testLogins[i])).scalars().first()
                        if existing_user is None:
                              user = User(
                                    full_name= f"{testSurnames[i]} {testNames[i]} {testPatrynomics[i]}",
                                    login=testLogins[i],
                                    password=testPasswords[i],
                              )
                              db.add(user)
                  db.commit()
                  return "INFO:     Synthetic users created"
            except Exception as e:
                  return f"ERROR:   {e}"