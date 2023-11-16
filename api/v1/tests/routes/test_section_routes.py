from cgi import test
from operator import le
from fastapi.testclient import TestClient
import pytest
from tests.main_test import (
    app,
)  # Replace with the actual path to your FastAPI app instance
import random
import string

client = TestClient(app)

test_sections_data = [
    {
        "id": "project_info",
        "name": "Project Information",
        "order": 1,
        "description": "Define the type of project you are working on.",
        "is_conditional": False,
    },
    {
        "id": "project_type",
        "name": "Project Type",
        "order": 2,
        "description": "Define the type of project you are working on.",
        "is_conditional": False,
    },
]
test_question_data = {
    # Your test data for a question
}
test_option_data = {
    # Your test data for an option
}


# Test for GET / - get_sections
@pytest.mark.sections_routes
def test_get_sections():
    response = client.get("/v1/sections/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 7


# Test for GET /by/{property}/{value} - find_section_by_property
@pytest.mark.sections_routes
def test_find_section_by_property():
    property = "id"  # Replace with an actual property
    value = "project_info"  # Replace with an actual value
    response = client.get(f"/v1/sections/by/{property}/{value}")
    assert response.status_code == 200
    assert response.json()[property] == value
    assert response.json()["name"] == "Project Information"


# Test for GET /{section_id}/next-section - get_next_section
@pytest.mark.sections_routes
def test_get_next_section():
    section_id = "project_info"  # Replace with an actual section_id
    response = client.get(f"/v1/sections/{section_id}/next-section")
    assert response.status_code == 200
    assert response.json()["id"] == "project_type"
    assert response.json()["name"] == "Project Type"


# Test for GET /next-questions - get_next_questions
@pytest.mark.sections_routes
def test_get_next_questions():
    question_id = "project_type"  # Replace with an actual question_id
    option_text = "Frontend"  # Replace with an actual option_text
    response = client.get(
        f"/v1/sections/next-questions?question_id={question_id}&option_text={option_text}"
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 1
    assert response.json()[0]["id"] == "frontend_framework"


# Test for GET /{section_id}/questions - get_questions_for_section
@pytest.mark.sections_routes
def test_get_questions_for_section():
    section_id = "project_info"  # Replace with an actual section_id
    response = client.get(f"/v1/sections/{section_id}/questions")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
