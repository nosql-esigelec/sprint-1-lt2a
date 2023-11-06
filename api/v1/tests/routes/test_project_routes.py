from re import T
from fastapi.testclient import TestClient
import pytest
from tests.main_test import app  # Replace with the actual path to your FastAPI app instance

client = TestClient(app)

# Initialize this with some test data
test_project_data = {"created_by":"653e4964f9e328a046420984",
                     "project_name":"Dev Project New",
                     "project_type":"Backend",
                     "project_architecture":"Microservices",
                     "project_tags":["sc"]}

@pytest.fixture(scope="module")
def created_project_id():
    # Setup code: Create a project
    response = client.post("/v1/projects/", json=test_project_data)
    assert response.status_code == 200
    project_data = response.json()
    yield project_data["pid"]  # This will be used as the project_id in later tests

    # Teardown code: Delete the project
    client.delete(f"/v1/projects/{project_data['pid']}")
# Test for POST /
@pytest.mark.projects_routes
def test_create_project():
    response = client.post("/v1/projects/", json=test_project_data)
    assert response.status_code == 200
    assert "pid" in response.json()
    assert response.json()["project_name"] == "Dev Project New"
    assert response.json()["project_type"] == "Backend"

# Test for GET /
@pytest.mark.projects_routes
def test_get_projects():
    response = client.get("/v1/projects/", params={"user_id": "653e4964f9e328a046420984"})
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert response.json()[0]["project_name"] == "Dev Project New"

# Test for GET /{project_id}
@pytest.mark.projects_routes
def test_get_project(created_project_id):
    response = client.get(f"/v1/projects/{created_project_id}")
    assert response.status_code == 200
    assert response.json()["pid"] == created_project_id
    assert response.json()["project_name"] == "Dev Project New"
    response = client.get(f"/v1/projects/{created_project_id}", params={"full": True})
    assert response.status_code == 200
    assert "package_manager" in response.json()

# Test for PUT /{project_id}
@pytest.mark.projects_routes
def test_update_project(created_project_id):
    updated_data = {"project_name": "Updated Test Project"}
    response = client.put(f"/v1/projects/{created_project_id}", json=updated_data)
    assert response.status_code == 200
    assert response.json()["project_name"] == "Updated Test Project"

# Test for DELETE /{project_id}
@pytest.mark.projects_routes
def test_delete_project(created_project_id):
    response = client.delete(f"/v1/projects/{created_project_id}")
    assert response.status_code == 200
    assert response.json()["result"] == "success"

# Test for GET /{project_id}/recommended-templates
# @pytest.mark.projects_routes
# def test_get_recommended_templates(created_project_id):
#     response = client.get(f"/v1/projects/{created_project_id}/recommended-templates")
#     assert response.status_code == 200
#     assert isinstance(response.json(), list)
#     assert response.json()[0]["template_name"] == "FastAPI"
#     assert response.json()[0]["template_type"] == "Backend"
#     assert response.json()[0]["template_architecture"] == "Microservices"
#     assert response.json()[0]["template_tags"] == ["sc"]
#     assert response.json()[0]["template_description"] == "FastAPI template for backend microservices"
