import pytest
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

	assert body_type == expected_body_type

def test_create_user():
	url = f"{root_url}/users"
	data = {
		"username": "User",
		"email": "test@test.com",
		"password": "123"
	}
	response = requests.post(url, headers=headers, data=json.dumps(data))
	assert response.status_code == 201
	user_id = response.json().get("id")

	user_url = f"{url}/{user_id}"
	response = requests.get(user_url)
	assert response.status_code == 200

	response_data = response.json()
	del response_data["id"]
	assert response_data == data



