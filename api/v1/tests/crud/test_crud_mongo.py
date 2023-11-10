import pytest
from api.v1.src.dependencies import get_mongo_db
from pymongo.errors import OperationFailure
# Setup MongoDB test databasepw


@pytest.fixture(scope='module')
def mongo_instance():
    db = get_mongo_db('test_db')
    yield db
    

@pytest.mark.crud_operations
def test_mongo_instance(mongo_instance):
    assert mongo_instance is not None


@pytest.mark.crud_operations
def test_create_index(mongo_instance):
    users_collection = mongo_instance["users"]
    try:
        users_collection.drop_index("username_1")
    except OperationFailure:
        pass 
    index_name = users_collection.create_index([("username", 1)], unique=True)
    assert index_name == "username_1"

@pytest.mark.crud_operations
def test_create(mongo_instance):
    users_collection = mongo_instance["users"]
    users_collection.drop()
    document = {"username": "johnny", "name": "John", "age": 30}
    insert_result = users_collection.insert_one(document)
    assert insert_result.inserted_id is not None
    assert isinstance(str(insert_result.inserted_id), str)
    assert len(str(insert_result.inserted_id)) == 24

@pytest.mark.crud_operations
def test_read(mongo_instance):
    users_collection = mongo_instance["users"]
    query = {"name": "John"}
    result = users_collection.find_one(query)
    assert isinstance(result, dict)
    assert result['name'] == "John"

@pytest.mark.crud_operations
def test_update(mongo_instance):
    # Access the 'users' collection
    users_collection = mongo_instance["users"]

    # Prepare the query and update data
    query = {"name": "John"}
    update_data = {"$set": {"age": 31}}  # Use $set for updating fields
    update_result = users_collection.update_one(query, update_data)
    assert update_result.modified_count > 0

    # Validate update
    updated_document = users_collection.find_one(query)
    assert updated_document is not None
    assert updated_document['age'] == 31

@pytest.mark.crud_operations
def test_delete(mongo_instance):
    # Access the 'users' collection
    users_collection = mongo_instance["users"]

    # Prepare the query
    query = {"name": "John"}

    # Delete the document
    delete_result = users_collection.delete_one(query)
    assert delete_result.deleted_count > 0

    # Validate deletion
    result = users_collection.find_one(query)
    assert result is None


