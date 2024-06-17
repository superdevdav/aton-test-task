from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from models import Customer

class CustomerRepository:
      @staticmethod
      def createSyntheticCustomers(db: Session):
            try:
                  testAccountNumbers = [74176, 12321, 96518, 78812, 94714]
                  testSurnames = ['Попов', 'Эдинсон', 'Зарецкий', 'Гагарина', 'Петрова']
                  testNames = ['Тихон', 'Ричард', 'Борис', 'Мария', 'Екатерина']
                  testPatrynomics = ['Попович', 'Эдуардович', 'Юрьевич', 'Михаиловна', 'Дмитриевна']
                  testBirthDates = [datetime(1999, 10, 13), datetime(2000, 8, 12), datetime(1995, 4, 5), datetime(1980, 9, 10), datetime(1985, 4, 14)]
                  testINNs = [68141, 85914, 88123, 94819, 54815]
                  testFullNameResponsibles = ['Иванов Иван Петрович', 'Иванов Иван Петрович', 'Орлова Анна Олеговна', 'Орлова Анна Олеговна', 'Горбушкин Игорь Александрович']
                  for i in range(len(testSurnames)):
                        # Проверяем существует ли клиент с такими данными
                        existing_customer = db.execute(select(Customer).filter_by(account_number=testAccountNumbers[i])).scalars().first()
                        if existing_customer is None:
                              customer = Customer(
                                    account_number=testAccountNumbers[i],
                                    surname=testSurnames[i],
                                    name=testNames[i],
                                    patrynomic=testPatrynomics[i],
                                    birth_date=testBirthDates[i],
                                    inn=testINNs[i],
                                    full_name_responsible=testFullNameResponsibles[i]
                              )
                              db.add(customer)
                  db.commit()
                  return "INFO:     Synthetic customers created"
            except Exception as e:
                  return f"ERROR:   {e}"