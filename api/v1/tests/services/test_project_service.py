from httpx import get
import pytest
from src.dependencies import get_mongo_db
from src.dependencies import get_neo4j_db
from src.services.projects_service import ProjectService  


# Setup ProjectService instance
@pytest.fixture(scope='module')
def project_service_instance():
    mongo_instance = get_mongo_db('test_db')
    neo4j_instance = get_neo4j_db()
    return ProjectService(mongo_instance, neo4j_instance)
# Fixture to create a project and return its ID
@pytest.fixture(scope='function')
def project_id_fixture(project_service_instance):
    project_data = {"project_name": "Test Project"}
    return project_service_instance.create_project(project_data).get("result")

@pytest.mark.project_service
def test_create_project(project_service_instance):
    project_data = {"project_name": "Another Test Project"}
    project_id = project_service_instance.create_project(project_data).get("result")
    assert isinstance(project_id, str)

@pytest.mark.project_service
def test_read_project(project_service_instance, project_id_fixture):
    project = project_service_instance.read_project(project_id_fixture).get("result")
    assert '_id' in project
    assert str(project['_id']) == project_id_fixture

@pytest.mark.project_service
def test_update_project(project_service_instance, project_id_fixture):
    update_data = {"project_name": "Updated Project"}
    update_result = project_service_instance.update_project(project_id_fixture, update_data).get("result")
    assert isinstance(update_result, str)

@pytest.mark.project_service
def test_delete_project(project_service_instance, project_id_fixture):
    delete_result = project_service_instance.delete_project(project_id_fixture).get("result")
    assert isinstance(delete_result, str)

@pytest.mark.project_service
def test_list_projects(project_service_instance):
    user_id = "some_user_id"
    projects = project_service_instance.list_projects(user_id).get("result")
    assert isinstance(projects, list)


