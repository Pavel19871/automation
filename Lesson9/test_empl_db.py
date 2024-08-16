import unittest
from unittest.mock import patch, MagicMock
from empl import Company  # Импортируйте класс Company, если он у вас есть
from EmplTable import EmployeeManager  # Импортируйте ваш класс

# Инициализация API и базы данных
api = Company("https://x-clients-be.onrender.com")
db = EmployeeManager("postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0")

def setup_module(module):
    db.delete_all_employees()  # Очищаем таблицу сотрудников перед тестами

def teardown_module(module):
    # Удалите эту строку, если dispose не определен
    pass

def test_create_and_get_employee():
    name = "SkyPro"
    descr = "testing"
    
    # Создание компании
    company = api.create_company(name, descr)
    assert company is not None, "Failed to create company"
    
    new_company_id = company.get("id")
    assert new_company_id is not None, "Company ID is missing in the response"

    len_before = len(db.get_employees())  # Получаем количество сотрудников до добавления

    # Добавляем нового сотрудника
    db.insert_employee("Mike", "Sorreto", "+123456789", new_company_id)

    len_after = len(db.get_employees())  # Получаем количество сотрудников после добавления

    assert len_after - len_before == 1, "Employee count did not increase as expected"

    employee_list = db.get_employees()  # Получаем список сотрудников компании
    assert any(employee.first_name == "Mike" and employee.last_name == "Sorreto" for employee in employee_list), "Employee not found in the employee list"

def test_update_employee():
    employees = db.get_employees()  # Получаем всех сотрудников
    assert len(employees) > 0, "No employees found"

    employee_id = employees[0].id  # Получаем ID первого сотрудника
    # Обновляем информацию о сотруднике
    db.update_employee(employee_id, "Jane", "Doe", "+987654321")

    updated_employee = db.get_employee_by_id(employee_id)  # Получаем обновленного сотрудника
    assert updated_employee.first_name == "Jane"
    assert updated_employee.last_name == "Doe"
    assert updated_employee.phone == "+987654321"

def test_delete_all_employees():
    employees = db.get_employees()  # Получаем всех сотрудников

    # Удаляем всех сотрудников
    for employee in employees:
        employee_id = employee.id  # Получаем ID сотрудника
        db.delete_employee(employee_id)

    employees_after_deletion = db.get_employees()  # Проверяем, что все сотрудники удалены
    assert len(employees_after_deletion) == 0, "Employees not deleted successfully"