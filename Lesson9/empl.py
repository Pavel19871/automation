import requests

class Company:
    def __init__(self, url: str):
        self.url = url

    def get_token(self, user='bloom', password='fire-fairy'):
        creds = {
            'username': user,
            'password': password
        }
        resp = requests.post(f"{self.url}/auth/login", json=creds)
        resp.raise_for_status()  # Поднимаем исключение, если запрос не удался
        return resp.json().get("userToken")  # Используем get для безопасного доступа к ключу

    def create_company(self, name, description=''):
        company = {
            "name": name,
            "description": description
        }
        my_headers = {
            "x-client-token": self.get_token()
        }
        resp = requests.post(f"{self.url}/company", json=company, headers=my_headers)
        resp.raise_for_status()  # Проверка на успешный ответ
        return resp.json()

    def get_list_employee(self, company_id):
        my_params = {
            "company": company_id
        }
        resp = requests.get(f"{self.url}/employee", params=my_params)
        resp.raise_for_status()  # Проверка на успешный ответ
        return resp.json()

    def get_employee_by_id(self, employee_id):
        resp = requests.get(f"{self.url}/employee/{employee_id}")
        resp.raise_for_status()  # Проверка на успешный ответ
        return resp.json()

    def add_new_employee(self, company_id, name, last_name):
        employee = {
            "firstName": name,
            "lastName": last_name,
            "middleName": "-",
            "companyId": company_id,
            "email": "test@test.ru",
            "url": "string",
            "phone": "89999999999",
            "birthdate": "2023-12-25T18:54:13.783Z",
            "isActive": True  # Исправлено на булево значение
        }

        my_headers = {
            "x-client-token": self.get_token()
        }
        resp = requests.post(f"{self.url}/employee", headers=my_headers, json=employee)
        resp.raise_for_status()  # Проверка на успешный ответ
        return resp.json()

    def update_employee_info(self, employee_id, last_name, email):
        user_info = {
            "lastName": last_name,
            "email": email,
            "isActive": True  # Исправлено на булево значение
        }

        my_headers = {
            "x-client-token": self.get_token()
        }
        resp = requests.patch(f"{self.url}/employee/{employee_id}", headers=my_headers, json=user_info)
        resp.raise_for_status()  # Проверка на успешный ответ
        return resp.json()
