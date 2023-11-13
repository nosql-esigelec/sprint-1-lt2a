from api.v1.src.services.users_service import UserService  # Replace with the actual import path
from api.v1.src.services.templates_service import TemplateService
from api.v1.src.dependencies import get_mongo_db
from api.v1.src.services.users_service import UserService
from api.v1.src.utils.handlers import random_string
from api.v1.src.dependencies import get_mongo_db #, get_neo4j_db
import ast 
from bson.objectid import ObjectId
from pymongo import MongoClient
from pymongo.server_api import ServerApi

db_instance = get_mongo_db(database_name='test_db')
#user_service_instance = UserService(db)
username = "John"
password = "secure_password"
#result = user_service_instance.get_user_by_username(username)
"""
#user_id = response['success']  # Extract 'result' key from response
template_service_instance = TemplateService(mongodb=db)
user_service_instance = UserService(mongodb=db)
"""
data = {"username": "Johna", "password": "secure_password"}
#response = user_service_instance.create_user(user_data=data)
#user_id = response['result']['result']
"""
template_name = "ReadTest"+random_string()
template_data = {"template_name": template_name, "is_private": False, "created_by": user_id}
#print(f"Template data in creation: {template_data}")
result = template_service_instance.create_template(template_data)
#print(result)
value = result['result']['value']
template_id = ast.literal_eval(value).get('result', None)
#print(template_id)
template = template_service_instance.read_template(template_id)
#print(f"Template: {template['result']['result']['result']['template_name']}")
# You should create some templates first to test the listing
created = []
template_name = "ListTest"+random_string()
template_data = {
        "template_name": template_name, 
        "is_private": True, 
        "created_by": user_id
    }
for i in range(3):
    template = template_service_instance.create_template(template_data)
    created.append(template)

templates = template_service_instance.list_templates(user_id)
templates = templates['result']['result']
#print(user_id)
#print(templates)
template_data = {"template_name": "DeleteTest"+random_string(), "is_private": False, "created_by": str(ObjectId())}
template_id = template_service_instance.create_template(template_data)
value = template_id['result']['value']
template_id = ast.literal_eval(value).get('result', None)
delete_result = template_service_instance.delete_template(template_id)
template_data = {"template_name": "DeleteTest"+random_string(), "is_private": False, "created_by": user_id}
template_id = template_service_instance.create_template(template_data)
#value = template_id['result']['value']
#template_id = ast.literal_eval(value).get('result', None)
#delete_result = template_service_instance.delete_template(template_id, user_id=user_id)

# Check if the delete operation returned the correct template ID
#print(delete_result)
print(template_id)
"""
user_service_instance = UserService(db=db_instance)
data = {"username": "John", "password": "secure_password"}
response = user_service_instance.create_user(user_data=data).get("result")

user_service_instance = UserService(db=db_instance)
data = {"username": "John", "password": "secure_password"}
user_id = user_service_instance.create_user(user_data=data).get("result")
template_service_instance=TemplateService(mongo=db_instance#, neo4j=neo4j_instance
                        )
#created = []
"""
for i in range(3):
    template = template_service_instance.create_template({
        "template_name": f"ListTest{random_string()}{i}", 
        "is_private": False, 
        "created_by": user_id
    }).get("result")
    created.append(template)
list = template_service_instance.list_templates().get("result")"""
#if templates and "templates" in templates['result']:
#    templates = templates["templates"]
#templates['result'] if 'template_name' in templates['result'] else ['No templates found']
# You need to create a template first to test the read operation
template_name = "StarTest"+random_string()
template_data = {"template_name": template_name, "is_private": True, "created_by": user_id}
template_id = template_service_instance.create_template(template_data).get("result")['id']['template_id']
# Perform the star operation
star = template_service_instance.star_template(user_id, template_id).get("result")
# Verify the template is starred by the user
starred_template = user_service_instance.read_user(user_id).get("result").get("starred_templates")
print(starred_template)