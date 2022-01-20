import requests


def test_get_users():
	url = "http://localhost:5000/users"
	response = requests.get(url)
	resp_type = type(response.json())

	assert resp_type == list

test_get_users()