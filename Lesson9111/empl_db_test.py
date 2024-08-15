import pytest
from Company import Company
from EmplTable import EmplTable

api = Company("https://x-clients-be.onrender.com")
db = EmplTable("postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com:5432/x_clients_db_fxd0?sslmode=require")
def setup_module(module):
    db.create_table()
    db.delete_all_employees()

def teardown_module(module):
    db.dispose()

def test_create_and_get_employee():
    name = "NameCompani"
    descr = "testing"
    company = api.create_company(name, descr)
    new_company_id = company["id"]

    len_before = len(db.get_employees())

    db.insert_employee("Nik", "One", "+711111111111", new_company_id)

    len_after = len(db.get_employees())

    assert len_after - len_before == 1

    employee_list = api.get_list_employee(new_company_id)
    assert any(employee["firstName"] == "Nik" and employee["lastName"] == "One" for employee in employee_list)

def test_update_employee():
    employees = db.get_employees()
    assert len(employees) > 0

    employee_id = employees[0]["id"]
    db.update_employee(employee_id, "Nastay", "Try", "Good", "+722222222222", "tester1@test.com", "http://nastaytry.com")

    updated_employee = db.get_employee_by_id(employee_id)
    assert updated_employee["first_name"] == "Nastay"
    assert updated_employee["last_name"] == "Try"
    assert updated_employee["middle_name"] == "Good"
    assert updated_employee["phone"] == "+722222222222"
    assert updated_employee["email"] == "tester1@test.com"
    assert updated_employee["avatar_url"] == "http://nastaytry.com"

def test_delete_all_employees():
    employees = db.get_employees()

    for employee in employees:
        employee_id = employee["id"]
        db.delete_employee(employee_id)

    employees_after_deletion = db.get_employees()
    assert len(employees_after_deletion) == 0