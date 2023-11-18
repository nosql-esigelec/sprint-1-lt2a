projects = [
    {
    'id': 'project1',
    'name':'Dev project',
    'description': 'This project is for development.'        
    },
    {
    'id': 'project2',
    'name':'goTrack',
    'description': 'This project is for Track.'        
    }
]

project_relations = [
    # Relations for project1 (Dev project)
    {'project_id': 'project1', 'section_id': 'programming_language', 'question_id': 'language', 'option_text': 'Python'},
    {'project_id': 'project1', 'section_id': 'programming_language', 'question_id': 'language_version', 'option_text': '3.9.7'},
    {'project_id': 'project1', 'section_id': 'project_type', 'question_id': 'project_type', 'option_text': 'Web Application'},
    {'project_id': 'project1', 'section_id': 'frameworks', 'question_id': 'backend_framework', 'option_text': 'Django'},
    {'project_id': 'project1', 'section_id': 'frameworks', 'question_id': 'frontend_framework', 'option_text': 'React'},
    {'project_id': 'project1', 'section_id': 'advanced_configurations', 'question_id': 'additional_configurations', 'option_text': 'Authentication'},
    {'project_id': 'project1', 'section_id': 'advanced_configurations', 'question_id': 'authentication_type', 'option_text': 'JWT'},
    {'project_id': 'project1', 'section_id': 'advanced_configurations', 'question_id': 'code_quality_type', 'option_text': 'Linting'},
    {'project_id': 'project1', 'section_id': 'advanced_configurations', 'question_id': 'database', 'option_text': 'PostgreSQL'},

    # Relations for project2 (goTrack)
    {'project_id': 'project2', 'section_id': 'programming_language', 'question_id': 'language', 'option_text': 'Golang'},
    {'project_id': 'project2', 'section_id': 'programming_language', 'question_id': 'language_version', 'option_text': '1.17'},
    {'project_id': 'project2', 'section_id': 'project_type', 'question_id': 'project_type', 'option_text': 'Backend Services'},
    {'project_id': 'project2', 'section_id': 'frameworks', 'question_id': 'backend_framework', 'option_text': 'Backend Services'},
    {'project_id': 'project2', 'section_id': 'advanced_configurations', 'question_id': 'additional_configurations', 'option_text': 'Containerization'},
    {'project_id': 'project2', 'section_id': 'advanced_configurations', 'question_id': 'containerization_type', 'option_text': 'Docker'},
    {'project_id': 'project2', 'section_id': 'advanced_configurations', 'question_id': 'code_quality_type', 'option_text': 'Static Analysis'},
    {'project_id': 'project2', 'section_id': 'advanced_configurations', 'question_id': 'database', 'option_text': 'MongoDB'},
]