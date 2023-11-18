
options =[
        {
      "text": "Monolithic",
      "is_default": True,
      "question_id": "project_architecture",
      "tags": ["Monolithic", "Single Codebase", "Simplicity"]
    },
    {
      "text": "Microservices",
      "is_default": False,
      "question_id": "project_architecture",
      "tags": ["Microservices", "Scalability", "Decoupling"]
    },
    {
      "text": "Serverless",
      "is_default": False,
      "question_id": "project_architecture",
      "tags": ["Serverless", "Event-driven", "Cost-Effective"]
    },
    {
      "text": "Event-Driven",
      "is_default": False,
      "question_id": "project_architecture",
      "tags": ["Event-Driven", "Asynchronous", "Scalability"]
    },
        {
            'text': 'Python',
            'is_default': True,
            'question_id': 'language',
            'version': ['3.9.7', '3.8.12', '3.7.12'],
            'tags': ['Python', 'Data Science', 'Web Development', 'Scripting', 'Machine Learning', 'Automation']
        },
        {
            'text': 'JavaScript',
            'is_default': False,
            'question_id': 'language',
            'version': ['ES11', 'ES10', 'ES9'],
            'tags': ['JavaScript', 'Frontend', 'Web Development', 'Real-time', 'Serverless']
        },
        {
            'text': 'Kotlin',
            'is_default': False,
            'question_id': 'language',
            'version': ['1.5.30', '1.5.21', '1.5.10'],
            'tags': ['Kotlin', 'Android', 'Mobile Application', 'Native', 'Cross-platform', 'JVM']
        },
        {
            'text': 'Golang',
            'is_default': False,
            'question_id': 'language',
            'version': ['1.17', '1.16.7', '1.15.15'],
            'tags': ['Golang', 'Microservices', 'Concurrency', 'Cloud Computing', 'DevOps'],
            
        },
        {
            'text': 'Swift',
            'is_default': False,
            'question_id': 'language',
            'version': ['5.4', '5.3.3', '5.2.4'],
            'tags': ['Swift', 'iOS', 'macOS', 'Mobile Applicatione', 'Server-side', 'Cross-platform']
        },
        {
            'text': 'Other',
            'is_default': False,
            'question_id': 'language',
            'version': [],
            'tags': []
        },
            {
        'text': 'Web Application',
        'is_default': True,
        'question_id': 'project_type',
        'applicable_languages': ['Python', 'JavaScript'],
        'tags': ['Frontend', 'Backend', 'Full-Stack', 'Web Services']
    },
    {
        'text': 'API Development',
        'is_default': False,
        'question_id': 'project_type',
        'applicable_languages': ['Python', 'JavaScript', 'Golang'],
        'tags': ['RESTful', 'GraphQL', 'Microservices', 'Serverless']
    },
    {
        'text': 'Data Science',
        'is_default': False,
        'question_id': 'project_type',
        'applicable_languages': ['Python'],
        'tags': ['Data Analysis', 'Machine Learning', 'Data Visualization', 'Statistics']
    },
    {
        'text': 'Android App',
        'is_default': False,
        'question_id': 'project_type',
        'applicable_languages': ['Kotlin'],
        'tags': ['Mobile', 'Native', 'Cross-platform', 'UI/UX']
    },
    {
        'text': 'iOS App',
        'is_default': False,
        'question_id': 'project_type',
        'applicable_languages': ['Swift'],
        'tags': ['Mobile', 'Native', 'Cross-platform', 'UI/UX']
    },
    {
        'text': 'Backend Services',
        'is_default': False,
        'question_id': 'project_type',
        'applicable_languages': ['Golang'],
        'tags': ['Microservices', 'Cloud Computing', 'DevOps', 'Concurrency']
    },
        {
        'text': 'Backend',
        'is_default': False,
        'question_id': 'project_type',
        'applicable_languages': ['Golang'],
        'tags': ['Microservices', 'API Development']
    },
            {
        'text': 'Frontend',
        'is_default': False,
        'question_id': 'project_type',
        'applicable_languages': ['Golang'],
        'tags': ['Web Application', 'Mobile Application']
    },
    {
        'text': 'Full-Stack',
        'is_default': False,
        'question_id': 'project_type',
        'applicable_languages': ['Golang'],
        'tags': ['Microservices', 'Cloud Computing', 'DevOps', 'Concurrency']
    },
    {
        'text': 'Other',
        'is_default': False,
        'question_id': 'project_type',
        'applicable_languages': [],
        'tags': []
    },
        {
        'text': 'Django',
        'is_default': True,
        'question_id': 'backend_framework',
        'applicable_languages': ['Python'],
        'applicable_project_types': ['Web Application'],
        'tags': ['Web Framework', 'Full-Stack', 'ORM', 'MTV']
    },
    {
        'text': 'FastAPI',
        'is_default': False,
        'question_id': 'backend_framework',
        'applicable_languages': ['Python'],
        'applicable_project_types': ['Web Application', 'API Development'],
        'tags': ['Web Framework', 'API', 'ASGI', 'Type Checking']
    },
    {
        'text': 'Flask',
        'is_default': False,
        'question_id': 'backend_framework',
        'applicable_languages': ['Python'],
        'applicable_project_types': ['Web Application', 'API Development'],
        'tags': ['Web Framework', 'Microservices', 'WSGI', 'RESTful']
    },
    {
        'text': 'React',
        'is_default': True,
        'question_id': 'frontend_framework',
        'applicable_languages': ['JavaScript'],
        'applicable_project_types': ['Web Application', 'Full-Stack'],
        'tags': ['JavaScript', 'Component-based', 'SPA']
    },
    {
        'text': 'Vue.js',
        'is_default': False,
        'question_id': 'frontend_framework',
        'applicable_languages': ['JavaScript'],
        'applicable_project_types': ['Web Application', 'Full-Stack'],
        'tags': ['JavaScript', 'Reactive', 'SPA']
    },
    {
        'text': 'Angular',
        'is_default': False,
        'question_id': 'frontend_framework',
        'applicable_languages': ['JavaScript', 'TypeScript'],
        'applicable_project_types': ['Web Application', 'Full-Stack'],
        'tags': ['JavaScript', 'TypeScript', 'MVVM']
    },
    {
        'text': 'SwiftUI',
        'is_default': False,
        'question_id': 'frontend_framework',
        'applicable_languages': ['Swift'],
        'applicable_project_types': ['iOS App', 'macOS App'],
        'tags': ['Swift', 'Declarative Syntax', 'Native']
    },
      {
        "text": "Spring Boot",
        "is_default": False,
        "question_id": "framework",
        "tags": ["Backend Services", "API Development"]
    },
    {
        "text": "TensorFlow",
        "is_default": False,
        "question_id": "framework",
        "tags": ["Data Science"]
    },
    {
        "text": "PyTorch",
        "is_default": False,
        "question_id": "framework",
        "tags": ["Data Science"]
    },
    {
        "text": "React Native",
        "is_default": False,
        "question_id": "framework",
        "tags": ["Android App", "iOS App"]
    },
    {
        "text": "Flutter",
        "is_default": False,
        "question_id": "framework",
        "tags": ["Android App", "iOS App"]
    },
    {
        'text': 'Bootstrap',
        'is_default': False,
        'question_id': 'frontend_framework',
        'applicable_languages': ['JavaScript', 'Python'],
        'applicable_project_types': ['Web Application', 'Full-Stack'],
        'tags': ['CSS', 'Layout', 'Components']
    },
    {
        'text': 'None/Not Sure',
        'is_default': False,
        'question_id': 'frontend_framework',
        'applicable_languages': [],
        'applicable_project_types': [],
        'tags': []
    },
        {
        'text': 'Authentication',
        'is_default': False,
        'question_id': 'additional_configurations',
        'tags': ['Authentication', 'Security']
    },
    {
        'text': 'Code Quality',
        'is_default': False,
        'question_id': 'additional_configurations',
        'tags': ['Code Quality', 'Security']
    },
    {
        'text': 'Testing',
        'is_default': False,
        'question_id': 'additional_configurations',
        'tags': ['Testing']
    },
    {
        'text': 'Containerization',
        'is_default': False,
        'question_id': 'additional_configurations',
        'tags': ['Docker', 'Containerization']
    },
    {
        'text': 'Package Management',
        'is_default': False,
        'question_id': 'additional_configurations',
        'tags': ['Package Management']
    },
        {
        'text': 'Database',
        'is_default': False,
        'question_id': 'additional_configurations',
        'tags': ['SQL', 'NoSQL']
    },
        {
        'text': 'PostgreSQL',
        'is_default': True,
        'question_id': 'database',
        'tags': ['SQL', 'ACID', 'Relational']
    },
    {
        'text': 'MongoDB',
        'is_default': False,
        'question_id': 'database',
        'tags': ['NoSQL', 'Document Store', 'Sharding']
    },
    {
        'text': 'SQLite',
        'is_default': False,
        'question_id': 'database',
        'tags': ['SQL', 'Embedded', 'Serverless']
    },
    {
        'text': 'Firebase Realtime Database',
        'is_default': False,
        'question_id': 'database',
        'tags': ['NoSQL', 'Real-time', 'Cloud']
    },
    {
        'text': 'Redis',
        'is_default': False,
        'question_id': 'database',
        'tags': ['In-memory', 'Key-Value Store', 'Cache']
    },
    {
        'text': 'None/Not Sure',
        'is_default': False,
        'question_id': 'database',
        'applicable_languages': [],
        'applicable_project_types': [],
        'tags': []
    },
        {
        'text': 'JWT',
        'is_default': True,
        'question_id': 'authentication_type',
        'tags': ['JWT', 'Token']
    },
    {
        'text': 'OAuth',
        'is_default': False,
        'question_id': 'authentication_type',
        'tags': ['OAuth', '3rd Party']
    },
    {
        'text': 'None',
        'is_default': False,
        'question_id': 'authentication_type',
        'tags': ['None']
    },
        {
        'text': 'Linting',
        'is_default': True,
        'question_id': 'code_quality_type',
        'tags': ['Linting', 'Syntax']
    },
    {
        'text': 'Static Analysis',
        'is_default': False,
        'question_id': 'code_quality_type',
        'tags': ['Static Analysis', 'Security']
    },
    {
        'text': 'Both',
        'is_default': False,
        'question_id': 'code_quality_type',
        'tags': ['Linting', 'Static Analysis']
    },
       {
        'text': 'Unit Tests',
        'is_default': True,
        'question_id': 'testing_type',
        'tags': ['Unit Tests']
    },
    {
        'text': 'Integration Tests',
        'is_default': False,
        'question_id': 'testing_type',
        'tags': ['Integration Tests']
    },
    {
        'text': 'Both',
        'is_default': False,
        'question_id': 'testing_type',
        'tags': ['Unit Tests', 'Integration Tests']
    },
        {
        'text': 'Docker',
        'is_default': True,
        'question_id': 'containerization_type',
        'tags': ['Docker']
    },
    {
        'text': 'None',
        'is_default': False,
        'question_id': 'containerization_type',
        'tags': ['None']
    },
        {
        'text': 'pip',
        'is_default': True,
        'question_id': 'package_manager',
        'tags': ['pip']
    },
    {
        'text': 'conda',
        'is_default': False,
        'question_id': 'package_manager',
        'tags': ['conda']
    },
    {
        'text': 'Hatch',
        'is_default': False,
        'question_id': 'package_manager',
        'tags': ['Hatch']
    },
    {
        'text': 'None',
        'is_default': False,
        'question_id': 'package_manager',
        'tags': ['None']
    },
        {
        'text': 'Yes',
        'is_default': True,
        'question_id': 'advanced_configurations',
        'tags': []
    },
            {
        'text': 'No',
        'is_default': False,
        'question_id': 'advanced_configurations',
        'tags': []
    },
    ]