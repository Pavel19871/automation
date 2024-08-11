from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.sql import text


class EmplTable:
    scripts = {
        "create": text("""
            CREATE TABLE IF NOT EXISTS employee (
                id SERIAL PRIMARY KEY,
                is_active BOOLEAN DEFAULT TRUE,
                create_timestamp TIMESTAMP DEFAULT now(),
                change_timestamp TIMESTAMP DEFAULT now(),
                first_name VARCHAR(20) NOT NULL,
                last_name VARCHAR(20) NOT NULL,
                middle_name VARCHAR(20),
                phone VARCHAR(15) NOT NULL,
                email VARCHAR(256),
                avatar_url VARCHAR(1024),
                company_id INTEGER NOT NULL
            )
        """),
         "select": text("SELECT * FROM employee"),
        "insert": text("""
            INSERT INTO employee (first_name, last_name, phone, company_id)
            VALUES (:first_name, :last_name, :phone, :company_id)
        """),
        "update": text("""
            UPDATE employee SET first_name = :first_name, last_name = :last_name,
            middle_name = :middle_name, phone = :phone, email = :email, avatar_url = :avatar_url
            WHERE id = :employee_id
        """),
        "delete": text("DELETE FROM employee WHERE id = :employee_id"),
        "delete_all": text("DELETE FROM employee"),
        "get_employee_by_id": text("SELECT * FROM employee WHERE id = :employee_id")
    }

    def __init__(self, connection_string):  # Исправлено __init__ на __init__
        self.__db = create_engine(connection_string, future=True)
        self.__metadata = MetaData()
        self.table = Table('employee', self.__metadata, autoload_with=self.__db)

    def create_table(self):
        with self.__db.connect() as conn:
            conn.execute(self.scripts["create"])  # Исправлено __scripts на scripts
            conn.commit()

    def get_employees(self):
        with self.__db.connect() as conn:
            result = conn.execute(self.scripts["select"])  # Исправлено __scripts на scripts
            return result.fetchall()

    def insert_employee(self, first_name, last_name, phone, company_id):
        with self.__db.connect() as conn:
            result = conn.execute(self.scripts["insert"],  # Исправлено __scripts на scripts
                                  {"first_name": first_name,
                                   "last_name": last_name,
                                   "phone": phone,
                                   "company_id": company_id})
            conn.commit()
            return result

    def update_employee(self, employee_id, first_name, last_name, middle_name, phone, email, avatar_url):
        with self.__db.connect() as conn:
            result = conn.execute(self.scripts["update"],  # Исправлено __scripts на scripts
                                  {"employee_id": employee_id,
                                   "first_name": first_name,
                                   "last_name": last_name,
                                   "middle_name": middle_name,
                                   "phone": phone,
                                   "email": email,
                                   "avatar_url": avatar_url})
            conn.commit()
            return result

    def get_employee_by_id(self, employee_id):
        with self.__db.connect() as conn:
            result = conn.execute(self.scripts["get_employee_by_id"], {"employee_id": employee_id})  # Исправлено __scripts на scripts
            return result.fetchone()

    def delete_employee(self, employee_id):
        with self.__db.connect() as conn:
            result = conn.execute(self.scripts["delete"], {"employee_id": employee_id})  # Исправлено __scripts на scripts
            conn.commit()
            return result

    def delete_all_employees(self):
        with self.__db.connect() as conn:
            result = conn.execute(self.scripts["delete_all"])  # Исправлено __scripts на scripts
            conn.commit()
            return result

    def dispose(self):
        self.__db.dispose()
        