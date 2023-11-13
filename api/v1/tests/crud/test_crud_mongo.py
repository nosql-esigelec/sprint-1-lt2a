import pytest
from src.dependencies import get_mongo_db
# Setup MongoDB test database


@pytest.fixture(scope='module')
def mongo_instance():
    db = get_mongo_db('test_db')
    yield db
    

@pytest.mark.crud_operations
def test_mongo_instance(mongo_instance):
    assert mongo_instance is not None


@pytest.mark.crud_operations
def test_create_index(mongo_instance):
    mongo_instance.drop_index("users", "username_1")
    index_name = mongo_instance.create_index("users", "username", unique=True).get("result")
    assert index_name == "username_1"

@pytest.mark.crud_operations
def test_create(mongo_instance):
    mongo_instance.drop_collection("users")
    document = {"username":"johnny", "name": "John", "age": 30}
    result = mongo_instance.create(document, "users").get("result")
    assert isinstance(result, str)
    assert len(result) == 24
    

@pytest.mark.crud_operations
def test_read(mongo_instance):
    query = {"name": "John"}
    result = mongo_instance.read(query, "users").get("result")
    assert isinstance(result, dict)
    assert result['name'] == "John"

@pytest.mark.crud_operations
def test_update(mongo_instance):
    query = {"name": "John"}
    update_data = {"age": 31}
    modified_count = mongo_instance.update(query, update_data, "users").get("result")
    assert modified_count > 0

    # Validate update
    updated_document = mongo_instance.read(query, "users").get("result")
    print(f"Updated document: {updated_document}")
    assert updated_document['age'] == 31

@pytest.mark.crud_operations
def test_delete(mongo_instance):
    query = {"name": "John"}
    deleted_count = mongo_instance.delete(query, "users").get("result")
    assert deleted_count > 0

    # Validate deletion
    result = mongo_instance.read(query, "users").get("result")
    assert result is None



