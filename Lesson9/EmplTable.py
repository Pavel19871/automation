from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.orm import declarative_base, sessionmaker  # Исправленный импорт
import logging

Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employees'
    
    id = Column(Integer, Sequence('employee_id_seq'), primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    phone = Column(String(20))
    company_id = Column(Integer)

class EmployeeManager:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def delete_all_employees(self):
        session = self.Session()
        try:
            session.query(Employee).delete()
            session.commit()
        except Exception as e:
            logging.error(f"Произошла ошибка: {e}")
            session.rollback()
        finally:
            session.close()

    def get_employees(self):
        session = self.Session()
        try:
            return session.query(Employee).all()
        except Exception as e:
            logging.error(f"Произошла ошибка: {e}")
            return []
        finally:
            session.close()

    def insert_employee(self, first_name, last_name, phone, company_id):
        session = self.Session()
        new_employee = Employee(first_name=first_name, last_name=last_name, phone=phone, company_id=company_id)
        try:
            session.add(new_employee)
            session.commit()
            return new_employee
        except Exception as e:
            logging.error(f"Произошла ошибка: {e}")
            session.rollback()
            return None
        finally:
            session.close()

    def update_employee(self, employee_id, first_name, last_name, phone):
        session = self.Session()
        try:
            employee = session.query(Employee).filter(Employee.id == employee_id).one()
            employee.first_name = first_name
            employee.last_name = last_name
            employee.phone = phone
            session.commit()
            return employee
        except Exception as e:
            logging.error(f"Произошла ошибка: {e}")
            session.rollback()
            return None
        finally:
            session.close()

    def delete_employee(self, employee_id):
        session = self.Session()
        try:
            employee = session.query(Employee).filter(Employee.id == employee_id).one()
            session.delete(employee)
            session.commit()
        except Exception as e:
            logging.error(f"Произошла ошибка: {e}")
            session.rollback()
        finally:
            session.close()

    def get_employee_by_id(self, employee_id):
        session = self.Session()
        try:
            return session.query(Employee).filter(Employee.id == employee_id).one()
        except Exception as e:
            logging.error(f"Произошла ошибка: {e}")
            return None
        finally:
            session.close()