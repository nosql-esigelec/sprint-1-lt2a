import pytest
from api.v1.src.dependencies import get_mongo_db
from api.v1.src.services.users_service import UserService  # Replace with the actual import path
from logging import info

# Setup MongoDB test database
@pytest.fixture(scope='module')
def db_instance():
    db = get_mongo_db(database_name='test_db')
    yield db


# Setup UserService instance
@pytest.fixture(scope='module')
def user_service_instance(db_instance):
    return UserService(db_instance)

@pytest.mark.user_service
def test_create_user(user_service_instance):
    user_data = {"username": "John", "password": "secure_password"}
    response = user_service_instance.create_user(user_data)

    user_id = response['result']['result']  # Extract 'result' key from response
    assert response['success'] is True
    assert isinstance(user_id, str)
    assert len(user_id) == 24

@pytest.mark.user_service
def test_authenticate_user(user_service_instance):
    username = "John"
    password = "secure_password"
    user = user_service_instance.authenticate_user(username, password)
    assert 'username' in user['result']['result']
    assert user['result']['result']['username'] == username

@pytest.mark.user_service
def test_read_user(user_service_instance):
    # Assume user_id is obtained from test_create_user or setup
    user_data = {"username": "John", "password": "secure_password"}
    user_id = user_service_instance.create_user(user_data)
    user_id = user_id['result']['result']
    user = user_service_instance.read_user(user_id)
    user = user['result']['result']
    assert '_id' in user
    assert str(user['_id']) == user_id

@pytest.mark.user_service
def test_get_user_by_username(user_service_instance):
    username = "John"
    result = user_service_instance.get_user_by_username(username)
    user = result['result']
    assert 'username' in user
    assert user['username'] == username