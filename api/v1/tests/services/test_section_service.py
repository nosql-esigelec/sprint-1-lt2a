import pytest
from bson.objectid import ObjectId
from api.v1.tests.services.test_user_service import user_service_instance
from src.services.sections_service import SectionService
from src.utils.handlers import random_string
from src.dependencies import get_mongo_db, get_neo4j_db

@pytest.fixture(scope='module')
def neo4j_instance():
    neo4j = get_neo4j_db()
    yield neo4j

@pytest.fixture(scope='module')
def section_service_instance(neo4j_instance):
    return SectionService(neo4j=neo4j_instance)
test_sections_data = [
           {
            'id': 'project_info',
            'name': 'Project Information',
            'order': 1,
            'description': 'Define the type of project you are working on.',
            'is_conditional': False
        },
        {
            'id': 'project_type',
            'name': 'Project Type',
            'order': 2,
            'description': 'Define the type of project you are working on.',
            'is_conditional': False
        }]



@pytest.mark.section_service
def test_get_sections(section_service_instance):
    sections = section_service_instance.get_sections()
    assert isinstance(sections, list)
    assert len(sections) == 7
    assert sections[0]["id"] == "project_info"
    
@pytest.mark.section_service
def test_find_section_by_property(section_service_instance):
    property = "id"
    value = "project_info"
    section = section_service_instance.get_section_by_property(property, value)
    assert isinstance(section, dict)
    assert section[property] == value
    assert section["name"] == "Project Information"


@pytest.mark.section_service
def test_get_next_section(section_service_instance):
    section_id = "project_info"
    next_section = section_service_instance.get_next_section(section_id)
    assert isinstance(next_section, dict)
    assert next_section["id"] == "project_type"
    assert next_section["name"] == "Project Type"

@pytest.mark.section_service
def test_get_questions_for_section(section_service_instance):
    section_id = "project_type"
    questions = section_service_instance.get_questions_for_section(section_id)
    assert isinstance(questions, list)
    assert len(questions) == 2
    assert questions[0]["id"] == "project_type"

@pytest.mark.section_service
def test_get_next_questions(section_service_instance):
    question_id = "project_type"
    option_text = "Frontend"
    questions = section_service_instance.get_next_questions(question_id, option_text)
    assert isinstance(questions, list)
    assert len(questions) == 1
    assert questions[0]["id"] == "frontend_framework"
    assert questions[0]["options"][0]["text"] == "React"

