import requests
import allure


class EmployeeApi:
    allure.step("api. Инициализация")

    def __init__(self, url: str):  # Конструктор принимает URL
        self.url = url

    @allure.step("api. Получить токен авторизации")
    def get_token(self, user='flora', password='nature-fairy') -> str:
        creds = {
            "username": user,
            "password": password
        }
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json().get("userToken", "")  # Используем get для безопасного извлечения токена

    @allure.step("api. Добавить компанию")
    def create_company(self, name: str, description="") -> dict:
        company = {
            "name": name,
            "description": description
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + '/company', json=company, headers=my_headers)
        return resp.json()

    @allure.step("api. Получить список сотрудников по id компании")
    def get_employee(self, id: int) -> dict:  
        resp = requests.get(self.url + '/employee?company=' + str(id))  # Преобразование id в строку
        if resp.status_code == 200:
            return resp.json()
        else:
            print("Ошибка ответа:", resp.text)  # Логируем текст ответа
            return {}

    @allure.step("api. Добавить сотрудника")
    def create_employee(self, first_name: str, last_name: str, middle_name: str, id_company: int, email: str, phone: str) -> dict:
        employee = {
            "firstName": first_name,
            "lastName": last_name,
            "middleName": middle_name,
            "companyId": id_company,
            "email": email,
            "phone": phone
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + '/employee', json=employee, headers=my_headers)
        return resp.json()

    @allure.step("api. Получить сотрудника по id")
    def employee_id(self, id: int) -> dict:  
        resp = requests.get(self.url + '/employee/' + str(id))  # Преобразование id в строку
        if resp.status_code == 200:
            try:
                return resp.json()
            except ValueError:
                print("Ответ не является корректным JSON:", resp.text)
                return {}
        else:
            print("Ошибка ответа:", resp.text)  # Логируем текст ответа
            return {}

    @allure.step("api. Изменить информацию о сотруднике")
    def employee_change(self, id: int, last_name="", email="", phone="") -> dict:  
        employee = {
            "lastName": last_name,
            "email": email,
            "phone": phone
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.patch(self.url + '/employee/' + str(id), json=employee, headers=my_headers)  # Преобразование id в строку
        return resp.json()
