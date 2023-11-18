import pytest
from httpx import get

from api.v1.src.dependencies import get_mongo_db, get_neo4j_db
from api.v1.src.services.projects_service import ProjectService

project_with_options = {
    "created_by": "653e4964f9e328a046420984",
    "project_name": "Dev Project New",
    "project_type": "Data Science",
    "project_architecture": "Monolith",
    "project_tags": ["backend", "microservices"],
}


# Setup ProjectService instance
@pytest.fixture(scope="module")
def project_service_instance():
    mongo_instance = get_mongo_db("test_db")
    neo4j_instance = get_neo4j_db()
    return ProjectService(mongo_instance, neo4j_instance)


# Fixture to create a project and return its ID
@pytest.fixture(scope="function")
def project_id_fixture(project_service_instance):
    project_data = {"project_name": "Test Project"}
    return project_service_instance.create_project(project_data).get("result")


@pytest.mark.project_service
def test_create_project(project_service_instance):
    project_data = {"project_name": "Another Test Project"}
    project_id = project_service_instance.create_project(project_data).get("result")
    assert isinstance(project_id, str)
    project_neo4j = project_service_instance.neo4j.read(
        tx_type="node",
        node_label="Project",
        properties={"project_name": "Another Test Project"},
    ).get("result")
    assert project_neo4j is not None
    assert project_neo4j["project_name"] == "Another Test Project"


@pytest.mark.project_service
def test_read_project(project_service_instance, project_id_fixture):
    project = project_service_instance.read_project(project_id_fixture).get("result")
    assert "_id" in project
    assert str(project["_id"]) == project_id_fixture


@pytest.mark.project_service
def test_update_project(project_service_instance, project_id_fixture):
    update_data = {"project_name": "Updated Project"}
    update_result = project_service_instance.update_project(
        project_id_fixture, update_data
    ).get("result")
    assert isinstance(update_result, str)


@pytest.mark.project_service
def test_delete_project(project_service_instance, project_id_fixture):
    delete_result = project_service_instance.delete_project(project_id_fixture).get(
        "result"
    )
    assert isinstance(delete_result, str)
    project_neo4j = project_service_instance.neo4j.read(
        tx_type="node", node_label="Project", properties={"pid": project_id_fixture}
    ).get("result")
    assert project_neo4j is None


@pytest.mark.project_service
def test_list_projects(project_service_instance):
    user_id = "some_user_id"
    projects = project_service_instance.list_projects(user_id).get("result")
    assert isinstance(projects, list)


@pytest.mark.project_service
def test_get_recommended_templates(project_service_instance):
    project_with_options_id = project_service_instance.create_project(
        project_with_options
    ).get("result")
    recommended_templates = project_service_instance.get_recommended_templates(
        project_with_options_id
    ).get("result")
    assert isinstance(recommended_templates, list)
    print(recommended_templates)
    assert len(recommended_templates) == 1
    assert recommended_templates[0]["template_name"] == "Cookiecutter Data Science"


@pytest.mark.project_service
def test_select_template(project_service_instance):
    project_with_options_id = project_service_instance.create_project(
        project_with_options
    ).get("result")
    template_id = project_service_instance.neo4j.read(
        tx_type="node",
        node_label="Template",
        properties={"template_name": "Cookiecutter Data Science"},
    ).get("result")["tid"]
    relation = project_service_instance.select_template(
        project_with_options_id, template_id
    ).get("result")
    assert relation[1] == "SELECTED"
    assert relation[0]["id"] == project_with_options_id
    assert relation[2]["tid"] == template_id
