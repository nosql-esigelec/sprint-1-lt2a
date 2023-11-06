from fastapi.testclient import TestClient
import pytest
from tests.main_test import app  # Replace with the actual path to your FastAPI app instance
import random
import string
client = TestClient(app)


def random_string(length=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

test_template_data = {
    "created_by": "653910690eccd12c6b60c3f3",
    "is_private": False,
    "template_name": "Cookiecutter DS Public For Testing"+ random_string(),
    "template_url": "https://github.com/drivendata/cookiecutter-data-science",
    "template_tags": [
        "ai",
        "ml",
        "data-science"
    ],
    "template_description": "A logical, reasonably standardized, but flexible project structure for doing and sharing data science work.",
    "template_tree": """
    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    """
}
private_template_sample = {
    "created_by": "653910690eccd12c6b60c3f3",
    "is_private": True,
    "template_name": "Cookiecutter DS Private For Testing"+ random_string(),
    "template_url": "https://github.com/drivendata/cookiecutter-data-science",
    "template_tags": [
        "ai",
        "ml",
        "data-science"
    ],
    "template_description": "A logical, reasonably standardized, but flexible project structure for doing and sharing data science work.",
    "template_tree": """
    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    """
}
@pytest.fixture(scope="module")
def created_template_id():
    # Setup: Create a template
    test_template_data["template_name"] = "Cookiecutter DS Public For Testing"+ random_string() 
    response = client.post("/v1/templates/", json=test_template_data)
    assert response.status_code == 200
    template_data = response.json()
    yield template_data["tid"]["value"]  # This will be used as the template_id in later tests

    # Teardown: Delete the template
    client.delete(f"/v1/templates/{template_data['tid']['value']}")

# Test for POST /
@pytest.mark.templates_routes
def test_create_template():
    response = client.post("/v1/templates/", json=test_template_data)
    assert response.status_code == 200
    assert "tid" in response.json()

    response = client.post("/v1/templates/", json=private_template_sample)
    assert response.status_code == 200
    assert "tid" in response.json()

# Test for GET /
@pytest.mark.templates_routes
def test_get_templates():
    response = client.get("/v1/templates/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

    response = client.get("/v1/templates/", params={"user_id": "653910690eccd12c6b60c3f3"})
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Test for GET /{template_id}
@pytest.mark.templates_routes
def test_get_template(created_template_id):
    response = client.get(f"/v1/templates/{created_template_id}")
    assert response.status_code == 200
    assert response.json()["tid"] == created_template_id

# Test for DELETE /{template_id}
@pytest.mark.templates_routes
def test_delete_template(created_template_id):
    response = client.delete(f"/v1/templates/{created_template_id}")
    assert response.status_code == 200
    assert response.json()["result"] == "success"

@pytest.fixture(scope="module")
def created_template_private_id():
    # Setup: Create a template
    private_template_sample["template_name"] = "Cookiecutter DS Private For Testing"+ random_string()
    response = client.post("/v1/templates/", json=private_template_sample)
    assert response.status_code == 200
    template_data = response.json()
    yield template_data["tid"]["value"]  # This will be used as the template_id in later tests

    # Teardown: Delete the template
    client.delete(f"/v1/templates/{template_data['tid']['value']}", params={"user_id": "653910690eccd12c6b60c3f3"})



# Test for GET /{template_id}
@pytest.mark.templates_routes
def test_get_private_template(created_template_private_id):
    response = client.get(f"/v1/templates/{created_template_private_id}", params={"user_id": "653910690eccd12c6b60c3f3"})
    assert response.status_code == 200
    assert response.json()["tid"] == created_template_private_id

# Test for DELETE /{template_id}
@pytest.mark.templates_routes
def test_delete_private_template(created_template_private_id):
    response = client.delete(f"/v1/templates/{created_template_private_id}", params={"user_id": "653910690eccd12c6b60c3f3"})
    assert response.status_code == 200
    assert response.json()["result"] == "success"