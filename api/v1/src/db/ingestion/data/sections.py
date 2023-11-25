"""
This module contains a list of sections with their respective attributes.

The `sections` list contains dictionaries, where each dictionary represents a section.
Each section has the following attributes:
- `id`: The unique identifier of the section.
- `name`: The name of the section.
- `order`: The order in which the section should be displayed.
- `description`: A description of the section.
- `is_conditional`: A boolean value indicating whether the section is conditional or not.

The `sections` list can be used to define the structure and attributes of sections in an application or form.
"""

sections = [
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
        },
        {
            'id': 'programming_language',
            'name': 'Programming Language',
            'order': 3,
            'description': 'Select your primary development language.',
            'is_conditional': False
        },
        {
            'id': "frameworks",
            'name': 'Frameworks',
            'order': 4,
            'description': 'Choose the frameworks you are interested in for your project.',
            'is_conditional': True
        },
        {
            'id':"additional",
            'name': 'Additional Configurations',
            'order': 5,
            'description': 'Decide if you want additional configurations',
            'is_conditional': False
        },
        
        {
            'id':"advanced_configurations",
            'name': 'Advanced Configurations',
            'order': 6,
            'description': 'Select the advanced configurations for your project.',
            'is_conditional': True
        },
                {
            'id':"configurations",
            'name': 'Configurations',
            'order': 7,
            'description': 'Specify additional configurations and requirements for your project.',
            'is_conditional': True
        }
    ]