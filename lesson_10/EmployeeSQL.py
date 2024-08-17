from sqlalchemy import create_engine, text
import allure


class EmployeeSQL:
    scripts = {
        "select by id_company": text("select * from employee where company_id = :company_id"),
        "delete by id": text("delete from employee where id =:id_to_delete"),
        "insert new": text("insert into employee(\"first_name\", \"last_name\", \"middle_name\", \"company_id\", \"email\", \"phone\") values (:first_name, :last_name, :middle_name, :company_id, :email, :phone)"),
        "get max id": text("select MAX(\"id\") from employee")
    }

    @allure.step("БД. Подключение к БД")
    def __init__(self, connection_string: str):
        self.__db = create_engine(connection_string).connect()

    @allure.step("БД. Получить сотрудников по id компании")
    def get_employees(self, my_params: str):
        if not isinstance(my_params, str):
            raise ValueError("company_id должен быть строкой")
        result = self.__db.execute(self.scripts["select by id_company"], {"company_id": my_params}).fetchall()
        return result if result else []  # Возвращаем пустой список, если нет записей

    @allure.step("БД. Удалить сотрудника по id")
    def delete(self, id: int):
        self.__db.execute(self.scripts["delete by id"], {"id_to_delete": id})

    @allure.step("БД. Создать сотрудника")
    def create(self, first_name: str, last_name: str, middle_name: str, company_id: int, email: str, phone: str):
        self.__db.execute(self.scripts["insert new"], {
            "first_name": first_name,
            "last_name": last_name,
            "middle_name": middle_name,
            "company_id": company_id,
            "email": email,
            "phone": phone
        })

    @allure.step("БД. Получить максимальный id сотрудника")
    def get_max_id(self) -> int:
        result = self.__db.execute(self.scripts["get max id"]).fetchone()
        return result[0] if result else 0  # Вернуть 0, если нет записей
