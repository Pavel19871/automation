from empl import Company


api = Company("https://x-clients-be.onrender.com")


def test_get_list_of_employees():
    name = "Pavel"
    descr = "test"
    company = api.create_company(name, descr)
    new_id = company["id"]
    employee_list = api.get_list_employee(new_id)
    assert len(employee_list) == 0


def test_add_new_employee():
    name = "Pavel"
    descr = "test"
    company = api.create_company(name, descr)
    new_id = company["id"]
    new_employee = api.add_new_employee(new_id, "Pavel99", "B")
    assert new_employee["id"] > 0

    resp = api.get_list_employee(new_id)
    assert resp[0]["companyId"] == new_id
    assert resp[0]["firstName"] == "Pavel99"
    assert resp[0]["isActive"] == True
    assert resp[0]["lastName"] == "B"


def test_get_employee_by_id():
    name = "Pavel"
    descr = "test"
    company = api.create_company(name, descr)
    new_id = company["id"]
    new_employee = api.add_new_employee(new_id, "Pavel99", "Ba")
    id_employee = new_employee["id"]
    get_info = api.get_employee_by_id(id_employee)
    assert get_info["firstName"] == "Pavel99"
    assert get_info["lastName"] == "Ba"


def test_change_employee_info():
    name = "Pavel"
    descr = "test"
    company = api.create_company(name, descr)
    new_id = company["id"]
    new_employee = api.add_new_employee(new_id, "Pavel99", "Bab")
    id_employee = new_employee["id"]

    update = api.update_employee_info(id_employee, "Lomak", "Pavel.Lomakin@gmail.com")
    assert update["id"] == id_employee
    assert update["email"] == "Pavel.Lomakin@gmail.com"
    assert update["isActive"] == True