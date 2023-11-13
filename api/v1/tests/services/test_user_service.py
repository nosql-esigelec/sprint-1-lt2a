import pytest
from src.dependencies import get_mongo_db
from src.services.users_service import UserService  # Replace with the actual import path

# Setup MongoDB test database
@pytest.fixture(scope='module')
def db_instance():
    db = get_mongo_db('test_db')
    yield db


# Setup UserService instance
@pytest.fixture(scope='module')
def user_service_instance(db_instance):
    return UserService(db_instance)

@pytest.mark.user_service
def test_create_user(user_service_instance):
    user_data = {"username": "John", "password": "secure_password"}
    user_id = user_service_instance.create_user(user_data).get("result")
    assert isinstance(user_id, str)
    #assert user id is a mongo id string
    assert len(user_id) == 24

@pytest.mark.user_service
def test_authenticate_user(user_service_instance):
    username = "John"
    password = "secure_password"
    user = user_service_instance.authenticate_user(username, password).get("result")
    assert 'username' in user
    assert user['username'] == username

@pytest.mark.user_service
def test_read_user(user_service_instance):
    # Assume user_id is obtained from test_create_user or setup
    user_data = {"username": "John", "password": "secure_password"}
    user_id = user_service_instance.create_user(user_data).get("result")
    user = user_service_instance.read_user(user_id).get("result")
    assert '_id' in user
    assert str(user['_id']) == user_id

@pytest.mark.user_service
def test_get_user_by_username(user_service_instance):
    username = "John"
    user = user_service_instance.get_user_by_username(username).get("result")
    assert 'username' in user
    assert user['username'] == username
