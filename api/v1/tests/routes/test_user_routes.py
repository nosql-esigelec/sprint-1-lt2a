from fastapi.testclient import TestClient
import pytest
from tests.main_test import app  # Replace with the actual path to your FastAPI app instance

client = TestClient(app)

# Initialize this with some test data
test_user_data = {
    "username": "test_user",
    "password": "test_password",
    "email": "test@email.com",

}

@pytest.fixture(scope="module")
def registered_user():
    # Setup: Register a user
    response = client.post("/v1/users/register", json=test_user_data)
    assert response.status_code == 200
    user_data = response.json()
    yield user_data  # This will be used as the user data in later tests

    # Teardown: (Optional) delete the registered user
    # client.delete(f"/delete/{user_data['user_id']}")

# Test for POST /register
@pytest.mark.users_routes
def test_register_user():
    response = client.post("/v1/users/register", json=test_user_data)
    assert response.status_code == 200
    assert "user_id" in response.json()

# Test for POST /login
@pytest.mark.users_routes
def test_login(registered_user):
    login_data = {"username": test_user_data["username"], "password": test_user_data["password"]}
    response = client.post("/v1/users/login", data=login_data)
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert "token_type" in response.json()
    assert "user" in response.json()

# Test for GET /
@pytest.mark.users_routes
def test_get_user(registered_user):
    username = test_user_data["username"]
    response = client.get("/v1/users/", params={"username": username})
    assert response.status_code == 200
    assert response.json()["username"] == username
