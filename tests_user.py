import requests
import json

root_url = "http://localhost:5000"
headers = {
    "accept": "application/json",
    "Content-Type": "application/json"
}

def test_get_users():
	url = f"{root_url}/users"
	response = requests.get(url)
	body_type = type(response.json())
	expected_body_type = list

	if body_type == expected_body_type:
		print(f"Test for get_users request PASSED. Expected data type is {expected_body_type}")
	else:
		print(f"Get_users test FAILED. Expected data type: {expected_body_type}. Actual data type: {body_type}")

def test_create_user():
	url = f"{root_url}/users"
	data = {
		"username": "User",
		"email": "test@test.com",
		"password": "123"
	}
	response = requests.post(url, headers=headers, data=json.dumps(data))

	if response.status_code == 201:
		print(f"Test for create_user request PASSED. User with data {data} was created successfully")
	else:
		print(f"Create_user test FAILED. Status code: {response.status_code}. Error: {response.json()}")