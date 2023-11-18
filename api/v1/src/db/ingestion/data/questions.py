questions = [
            {
            'statement': 'Project Name',
            'id':'project_name',
            'question_type': 'text',
            'is_first': True,
            'required': True,
            'section_id': 'project_info',
            'order': 1
        },
        {
            'statement': 'Tags',
            'id': 'project_tags',
            'question_type': 'chips',
            'is_first': False,
            'required': True,
            'section_id': 'project_info',
            'order': 2
        },
        {
            'statement': 'Which language?',
            'id':'language',
            'question_type': 'multiselect',
            'is_first': True,
            'required': True,
            'section_id': 'programming_language',
            'order': 1
        },
        {
            'statement': 'Which version(s)?',
            'id': 'language_version',
            'question_type': 'chips',
            'is_first': False,
            'required': True,
            'section_id': 'programming_language',
            'order': 2
        },
        {
            'statement': 'What type of project are you working on?',
            'id': 'project_type',
            'question_type': 'select',
            'is_first': True,
            'required': True,
            'section_id': 'project_type',
            'order': 1
        },
        {
            'statement': 'What is the arcitecture Pattern?',
            'id': 'project_architecture',
            'question_type': 'select',
            'is_first': False,
            'required': False,
            'section_id': 'project_type',
            'order': 2
        },
        {
            'statement': 'Which framework are you interested in? ',
            'id': 'framework',
            'question_type': 'select',
            'is_first': False,
            'required': True,
            'section_id': 'frameworks',
            'order': 3,
            'depends_on': 'project_type',
            'value': ['Backend Services', 'API Development','Data Science', 'Android App', 'iOS App']
          
        },
        {
            'statement': 'Which back-end framework are you interested in? ',
            'id': 'backend_framework',
            'question_type': 'select',
            'is_first': False,
            'required': True,
            'section_id': 'frameworks',
            'order': 3,
            'depends_on': 'project_type',
            'value': ['Backend','Full-Stack']
          
        },
        {
            'statement': 'Which front-end framework are you interested in?',
            'id': 'frontend_framework',
            'question_type': 'select',
            'is_first': False,
            'required': True,
            'section_id': 'frameworks',
            'order': 2,
            'depends_on': 'project_type',
            'value': ['Frontend','Full-Stack','Web Application']
        },
        {
            'statement': 'If you want to add advanced configurations, click on "Next", otherwise click on "Get Templates".',
            'id': 'add_advanced_configurations',
            'question_type': 'statement',
            'is_first': True,
            'required': True,
            'section_id': 'additional',
            'order': 1
        },
        {
            'statement': 'Which advanced configurations do you want to do?',
            'id': 'additional_configurations',
            'question_type': 'multiselect',
            'is_first': True,
            'required': True,
            'section_id': 'advanced_configurations',
            'order': 1
        },
        {
            'statement': 'Which authentication features?',
            'id': 'authentication_type',
            'question_type': 'select',
            'is_first': False,
            'required': True,
            'section_id': 'configurations',
            'order': 2,
            'depends_on': 'additional_configurations',
            'value': ["Authentication"]
            
        },
        {
            'statement': 'What code quality tools do you want? ',
            'id': 'code_quality_type',
            'question_type': 'multiselect',
            'is_first': False,
            'required': True,
            'section_id': 'configurations',
            'order': 3,
            'depends_on': 'additional_configurations',
            'value': ["Code Quality"]
        },
                      {
            'statement': 'Which tests do you want? ',
            'id': 'testing_type',
            'question_type': 'multiselect',
            'is_first': False,
            'required': True,
            'section_id': 'configurations',
            'order': 4,
            'depends_on': 'additional_configurations',
            'value': ["Testing"]
        },
        {
            'statement': 'Which Contenerization tool do you want? ',
            'id': 'containerization_type',
            'question_type': 'select',
            'is_first': False,
            'required': True,
            'section_id': 'configurations',
            'order': 4,
            'depends_on': 'additional_configurations',
            'value': ["Containerization"]
        },
        {
            'statement': 'What is your preferred package/environment manager for Python?',
            'id': 'package_manager',
            'question_type': 'select',
            'is_first': False,
            'required': True,
            'section_id': 'configurations',
            'order': 5,
            'depends_on': 'additional_configurations',
            'value': ["Package Management"]
        },
        {
            'statement': 'Which databases do you want?',
            'id': 'database',
            'question_type': 'select',
            'is_first': False,
            'required': True,
            'section_id': 'configurations',
            'order': 6,
            'depends_on': 'additional_configurations',
            'value': ["Database"]
        }
    ]