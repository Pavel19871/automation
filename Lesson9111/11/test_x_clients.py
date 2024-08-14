from Emplloyee import Employer 
from dataBase import dataBase

api = Employer("https://x-clients-be.onrender.com")
db = dataBase("postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0")

def test_get_list_of_employers():
    db.create_company('Pavel testers', 'Pavel_company')
    max_id = db.last_company_id()
    db.create_employer(max_id, "Pavel", "Lomakin", 89993334455)
    db_employer_list = db.get_list_employer(max_id)
    api_employer_list = api.get_list(max_id)
    assert len(db_employer_list) == len(api_employer_list) 
    response = (api.get_list(max_id)) [0]
    employer_id = response["id"]
    db.delete_employer(employer_id)
    db.delete(max_id)
    
def test_add_new_employer():
    db.create_company('Pavel adding new employer', 'employer')
    max_id = db.last_company_id()
    db.create_employer(max_id, "Pavel", "Lomakin", 89993334455)
    response = (api.get_list(max_id))[0]
    employer_id = response ["id"] 
    assert response["companyId"] == max_id
    assert response["firstName"] == "Pavel"
    assert response["isActive"] == True
    assert response["lastName"] =="Lomakin"
    db.delete_employer(employer_id)
    db.delete(max_id)  
    
def test_assertion_data():
    db.create_company('Employer get id company', 'new')
    max_id = db.last_company_id
    db.create_employer(max_id, "Pavel", "Lomakin", 89993334455)
    employer_id = db.get_employer_id(max_id)
    get_api_info = (api.get_info(employer_id)).json()
    assert get_api_info["firstName"] == "Pavel"
    assert get_api_info["lastName"] == "Lomakin"
    assert get_api_info["phone"] == "89993334455"
    db.delete_employer(employer_id)
    db.delete(max_id)
    
def update_user_info():
    db.create_company('New updating company', 'test')
    max_id = db.last_company_id()
    db.create_employer(max_id, "Pavel", "Lomakin", 89993334455)
    employer_id = db.get_employer_id(max_id)
    db.update_employer_info("Leon", employer_id)
    get_api_info = (api.get_info(employer_id)).json()
    assert get_api_info["firstName"] == "Leon"
    assert get_api_info["lastName"] == "Lomakin"
    assert get_api_info["isActive"] == True
    db.delete_employer(employer_id)
    db.delete(max_id)    
        