import pytest
import ast
from bson.objectid import ObjectId
from api.v1.tests.services.test_user_service import user_service_instance
from api.v1.src.services.templates_service import TemplateService
from api.v1.src.services.users_service import UserService
from api.v1.src.utils.handlers import random_string
from api.v1.src.dependencies import get_mongo_db #, get_neo4j_db

@pytest.fixture(scope='module')
def mongo_instance():
    mongo = get_mongo_db('test_db')
    yield mongo


@pytest.fixture(scope='module')
def neo4j_instance():
    #neo4j = get_neo4j_db()
    #yield neo4j
    pass


@pytest.fixture(scope='module')
def template_service_instance(mongo_instance #, neo4j_instance
                            ):
    return TemplateService(mongodb=mongo_instance #, neo4j=neo4j_instance
                    )

@pytest.fixture(scope="module")
def user_id(mongo_instance):
    user_service_instance = UserService(mongodb=mongo_instance)
    data = {"username": "John", "password": "secure_password"}
    response = user_service_instance.create_user(user_data=data)
    user_id = response['result']['result']
    return user_id

@pytest.mark.template_service
def test_create_template(template_service_instance, user_id):
    template_name = "ReadTest"+random_string()
    template_data = {"template_name": template_name, "is_private": False, "created_by": user_id}
    print(f"Template data in creation: {template_data}")
    result = template_service_instance.create_template(template_data)
    result = result['result']
    print(f"Result: {result}")
    assert 'value' in result
    value = result['value']
    id = ast.literal_eval(value).get('result', None)
    # If the template is not private, it should be in the 'templates' collection
    if not template_data["is_private"]:
        inserted_template = template_service_instance.mongo.read(
            query={"_id": ObjectId(id)},
            collection_name="templates"
        )
        inserted_template = inserted_template['result']
        assert inserted_template is not None

@pytest.mark.template_service
def test_read_template(template_service_instance, user_id):
    # You need to create a template first to test the read operation
    template_name = "ReadTest"+random_string()
    template_data = {"template_name": template_name, "is_private": False, "created_by": user_id}
    print(f"Template data in creation: {template_data}")
    result = template_service_instance.create_template(template_data)
    value = result['result']['value']
    template_id = ast.literal_eval(value).get('result', None)
    print(template_id)
    template = template_service_instance.read_template(template_id)
    template = template['result']['result']['result']
    print(f"Template: {template}")
    assert 'template_name' in template
    assert template['template_name'] == template_name

@pytest.mark.template_service
def test_list_templates(template_service_instance, user_id):

    # You should create some templates first to test the listing
    for i in range(3):
        template_service_instance.create_template({
            "template_name": f"ListTest{random_string()}{i}", 
            "is_private": True, 
            "created_by": user_id
        })

    templates = template_service_instance.list_templates(user_id)
    templates = templates['result']['result']
    list_of_templates = [
    {
        'created_by': templates['created_by'][i],
        'is_private': templates['is_private'][i],
        'template_name': templates['template_name'][i]
    } for i in range(len(templates['created_by']))
    ]
    
    assert isinstance(list_of_templates, list)
    assert len(list_of_templates) >= 3  # Check if at least 3 templates were listed

@pytest.mark.template_service
def test_delete_template(template_service_instance, user_id):
    # You need to create a template first to test the delete operation
    template_data = {"template_name": "DeleteTest"+random_string(), "is_private": False, "created_by": str(ObjectId())}
    template_id = template_service_instance.create_template(template_data)
    value = template_id['result']['value']
    template_id = ast.literal_eval(value).get('result', None)
    delete_result = template_service_instance.delete_template(template_id)
    
    # Check if the delete operation returned the correct template ID
    assert delete_result == template_id
    # Verify the template no longer exists in the 'templates' collection
    deleted_template = template_service_instance.mongo.read(
        query={"_id": ObjectId(template_id)},
        collection_name="templates"
    )
    deleted_template = deleted_template['result']
    assert deleted_template is None

@pytest.mark.template_service
def test_delete_private_template(template_service_instance, user_id):
    # You need to create a template first to test the delete operation
    template_data = {"template_name": "DeleteTest"+random_string(), "is_private": True, "created_by": user_id}
    template_id = template_service_instance.create_template(template_data)

    delete_result = template_service_instance.delete_template(template_id, user_id=user_id)
    
    # Check if the delete operation returned the correct template ID
    assert delete_result == template_id
    # Verify the template no longer exists in the 'templates' collection
    deleted_template = template_service_instance.mongo.read(template_id, user_id=user_id)
    deleted_template = deleted_template['result']
    assert deleted_template is None

@pytest.mark.template_service
def test_star_template(template_service_instance, user_id):
    # You need to create a template first to test the star operation
    template_name = "StarTest"+random_string()
    template_data = {"template_name": template_name, "is_private": True, "created_by": user_id}
    template_id = template_service_instance.create_template(template_data)
    assert template_id == 0
    """
    # Perform the star operation
    template_service_instance.star_template(user_id, template_data["template_name"])
    # Verify the template is starred by the user
    starred_template = user_service_instance.read_user(user_id)
    
    assert starred_template is not None
    assert starred_template[0]["template_name"] == template_name"""    