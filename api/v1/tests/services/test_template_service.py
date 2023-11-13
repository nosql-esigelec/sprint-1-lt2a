import pytest
from bson.objectid import ObjectId
from api.v1.tests.services.test_user_service import user_service_instance
from src.services.templates_service import TemplateService
from src.services.users_service import UserService
from src.utils.handlers import random_string
from src.dependencies import get_mongo_db, get_neo4j_db

@pytest.fixture(scope='module')
def mongo_instance():
    mongo = get_mongo_db('test_db')
    yield mongo


@pytest.fixture(scope='module')
def neo4j_instance():
    neo4j = get_neo4j_db()
    yield neo4j


@pytest.fixture(scope='module')
def template_service_instance(mongo_instance, neo4j_instance):
    return TemplateService(mongo=mongo_instance, neo4j=neo4j_instance)
mongo = get_mongo_db('test_db')
user_service_instance = UserService(db=mongo)
user_id = user_service_instance.create_user({"username": "John", "password": "secure_password"}).get("result")

@pytest.mark.template_service
def test_create_template(template_service_instance):
    template_name = "ReadTest"+random_string()
    template_data = {"template_name": template_name, "is_private": False, "created_by": user_id}
    print(f"Template data in creation: {template_data}")
    result = template_service_instance.create_template(template_data).get("result")
    print(f"Result: {result}")
    assert 'value' in result
    # If the template is not private, it should be in the 'templates' collection
    if not template_data["is_private"]:
        inserted_template = template_service_instance.mongo.read(
            query={"_id": ObjectId(result['value'])},
            collection_name="templates"
        ).get("result")
        assert inserted_template is not None

@pytest.mark.template_service
def test_read_template(template_service_instance):
    # You need to create a template first to test the read operation
    template_name = "ReadTest"+random_string()
    template_data = {"template_name": template_name, "is_private": False, "created_by": user_id}
    print(f"Template data in creation: {template_data}")
    template_id = template_service_instance.create_template(template_data).get("result").get("value")
    print(f"Template ID: {template_id}")
    template = template_service_instance.read_template(template_id).get("result")
    print(f"Template: {template}")
    assert 'template_name' in template
    assert template['template_name'] == template_name

@pytest.mark.template_service
def test_list_templates(template_service_instance):

    # You should create some templates first to test the listing
    for i in range(3):
        template_service_instance.create_template({
            "template_name": f"ListTest{random_string()}{i}", 
            "is_private": True, 
            "created_by": user_id
        }).get("result")

    templates = template_service_instance.list_templates(user_id).get("result")

    
    assert isinstance(templates, list)
    assert len(templates) >= 3  # Check if at least 3 templates were listed
    for i in range(3):
        template_service_instance.create_template({
            "template_name": f"ListTest{random_string()}{i}", 
            "is_private": False, 
            "created_by": user_id
        }).get("result")
    templates = template_service_instance.list_templates().get("result")
    assert isinstance(templates, list)
    assert len(templates) >= 3  # Check if at least 3 templates were listed

@pytest.mark.template_service
def test_delete_template(template_service_instance):
    # You need to create a template first to test the delete operation
    template_data = {"template_name": "DeleteTest"+random_string(), "is_private": False, "created_by": str(ObjectId())}
    template_id = template_service_instance.create_template(template_data).get("result").get("value")
    
    delete_result = template_service_instance.delete_template(template_id).get("result")
    
    # Check if the delete operation returned the correct template ID
    assert delete_result == 1
    # Verify the template no longer exists in the 'templates' collection
    deleted_template = template_service_instance.mongo.read(
        query={"_id": ObjectId(template_id)},
        collection_name="templates"
    ).get("result")
    assert deleted_template is None

@pytest.mark.template_service
def test_delete_private_template(template_service_instance):
    # You need to create a template first to test the delete operation
    template_data = {"template_name": "DeleteTest"+random_string(), "is_private": True, "created_by": user_id}
    template_id = template_service_instance.create_template(template_data).get("result").get("value")
    
    delete_result = template_service_instance.delete_template(template_id, user_id=user_id).get("result")
    
    # Check if the delete operation returned the correct template ID
    assert delete_result == 1
    # Verify the template no longer exists in the 'templates' collection
    deleted_template = template_service_instance.read_template(template_id, user_id=user_id).get("result")
    assert deleted_template is None

@pytest.mark.template_service
def test_star_template(template_service_instance):
    # You need to create a template first to test the star operation
    template_name = "StarTest"+random_string()
    template_data = {"template_name": template_name, "is_private": True, "created_by": user_id}
    template_id = template_service_instance.create_template(template_data).get("result").get("value")
    # Perform the star operation
    template_service_instance.star_template(user_id, template_data["template_name"])
    # Verify the template is starred by the user
    starred_template = user_service_instance.read_user(user_id).get("result").get("starred_templates")
    
    assert starred_template is not None
    assert starred_template[0]["template_name"] == template_name    

