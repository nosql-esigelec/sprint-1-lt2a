admin_id = "653e4964f9e328a046420984"
is_private = False
templates = [
        {   'created_by': admin_id,
            'is_private': is_private,
            'template_name': 'Cookiecutter Data Science',
            'template_url': 'https://github.com/drivendata/cookiecutter-data-science',
            'template_description': 'A logical, reasonably standardized, but flexible project structure for doing and sharing data science work.',
            'template_tags': ['Python', 'Data Science', 'Machine Learning', 'Data Analysis'],
            'recommended_by': ['Data Science', 'Machine Learning', 'Data Analysis'],
            "template_tree": """
├── LICENSE
├── Makefile           <- Makefile with commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default Sphinx project; see sphinx-doc.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited template_description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Scripts to download or generate data
│   │   └── make_dataset.py
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling
│   │   └── build_features.py
│   │
│   ├── models         <- Scripts to train models and then use trained models to make
│   │   │                 predictions
│   │   ├── predict_model.py
│   │   └── train_model.py
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
│
└── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io
"""

        },
        {'created_by': admin_id,
         'is_private': is_private,
            'template_name': 'Cookiecutter Django',
            'template_url': 'https://github.com/pydanny/cookiecutter-django',
            'template_description': 'A bleeding edge Django project template with Bootstrap 5, customizable users app, starter templates, working user registration, celery setup, and much more.',
            'template_tags': ['Python', 'Django', 'Web Application','Frontend', 'Amazon S3', 'Google Cloud Storage', 'Azure Storage ', 'Docker Compose', 'Heroku', 'PostgreSQL', 'Pre Commit', 'Sentry'],
            'recommended_by':['Django', 'API', 'Backend'],
            'template_tree':""
        },
        {'created_by': admin_id,
         'is_private': is_private,
            'template_name': 'Cookiecutter Django Vue',
            'template_url': 'https://github.com/vchaptsev/cookiecutter-django-vue',
            'template_description': 'Cookiecutter Django Vue is a template for Django-Vue-Bootstrap projects.',
            'template_tags': ['Python', 'Django', 'Vue.js', 'Web Application','Frontend' 'PWA', 'API','REST','GraphQL', 'Sentry'],
            'recommended_by':['Django', 'API', 'Backend', 'Frontend', 'Vue.js'],
            'template_tree':""
        },
        {'created_by': admin_id,
         'is_private': is_private,
            'template_name': 'Wagtail Cookiecutter Foundation',
            'template_url': 'https://github.com/chrisdev/wagtail-cookiecutter-foundation',
            'template_description': 'A cookiecutter template for Wagtail CMS was built using Zurb Foundation front-end framework.',
            'template_tags': ['Python', 'Django', 'Zurb', 'Web Application', 'CMS', ],
            'recommended_by':['Django', 'CMS'],
            'template_tree':""
        },
        {'created_by': admin_id,
         'is_private': is_private,
            'template_name': 'Wemake Django Template',
            'template_url': 'https://github.com/wemake-services/wemake-django-template',
            'template_description': 'Bleeding edge django4.2 template focused on code quality and security.',
            'template_tags': ['Python', 'Django', 'Pytest', 'Flake8', 'Sphinx','Gitlab CI'],
            'recommended_by':['Django'],
            'template_tree':""
        },
        {'created_by': admin_id,
         'is_private': is_private,
            'template_name': 'Full Stack Fastapi Postgresql',
            'template_url': 'https://github.com/tiangolo/full-stack-fastapi-postgresql',
            'template_description': 'Full stack, modern web application generator. Using FastAPI, PostgreSQL as database, Docker, automatic HTTPS and more.',
            'template_tags': ['Python', 'FastAPI', 'PostgreSQL', 'Web Application', 'Docker Compose', 'Docker Swarm', 'JWT token', 'Celery', 'SQLAlchemy', 'Vue.js', 'TypeScript', 'Traefik', 'Gitlab CI'],
            'recommended_by':['FastAPI', 'PostgreSQL', 'Full-Stack', 'Frontend','Backend', 'Vue.js', 'TypeScript'],
            'template_tree':""
            
       
        },
        {'created_by': admin_id,
         'is_private': is_private,
            'template_name': 'Kotlin Android Mvvm Starter',
            'template_url': 'https://github.com/ribot/android-starter',
            'template_description': 'A Kotlin Android MVVM Starter template.',
            'template_tags': ['Kotlin', 'Android', 'Mobile Application'],
            'recommended_by': ['Kotlin', 'Android', 'Mobile Application'],
            'template_tree':""
            
        },
        {'created_by': admin_id,
         'is_private': is_private,
            'template_name': 'Swift Framework Template',
            'template_url': 'https://github.com/sbertix/Swift-Framework-Template',
            'template_description': 'A template for new Swift Framework.',
            'template_tags': ['Swift', 'iOS', 'Framework', 'TravisCI'],
            'recommended_by': ['Swift', 'iOS', 'Framework'],
            'template_tree':""
        },
        {'created_by': admin_id,
         'is_private': is_private,
            'template_name': 'Cookiecutter Golang',
            'template_url': 'https://github.com/lacion/cookiecutter-golang',
            'template_description': 'A Go application Dockerized cookiecutter template with batteries included.',
            'template_tags': ['Golang', 'Backend Services','Viper', 'Cobra', 'Logrus', 'Docker', 'TravisCI', 'CircleCI'],
            'recommended_by': ['Golang'],
            'template_tree':""
        },
        {'created_by': admin_id,
         'is_private': is_private,
            'template_name': 'Cookiecutter Flask',
            'template_url': 'https://github.com/cookiecutter-flask/cookiecutter-flask',
            'template_description': 'A Flask template for cookiecutter. (Supports Python ≥ 3.8)',
            'template_tags': ['Python', 'Flask', 'SQLAlchemy','Authentication'],
            'recommended_by': ['Flask', 'Authentication'],
            'template_tree':""
        },
        {'created_by': admin_id,
         'is_private': is_private,
            'template_name': 'Cookiecutter Flask Restful',
            'template_url': 'https://github.com/karec/cookiecutter-flask-restful',
            'template_description': 'Flask cookiecutter template for builing APIs with flask-restful, including JWT auth, cli, tests, swagger, docker and more',
            'template_tags': ['Python', 'Flask', 'SQLAlchemy','Authentication', 'Dotenv','API'],
            'recommended_by': ['Flask', 'API', 'Authentication'],
            'template_tree':""
        },
        {'created_by': admin_id,
         'is_private': is_private,
            'template_name': 'Flask Empty',
            'template_url': 'https://github.com/italomaia/flask-empty',
            'template_description': 'Flask-Empty is a simple flask boilerplate for fast prototyping. Just use cookiecutter and create a new project in no time.',
            'template_tags': ['Python', 'Flask'],
            'recommended_by': ['Flask'],
            'template_tree':""
        },
        {'created_by': admin_id,
         'is_private': is_private,
            'template_name': 'FastAPI + React',
            'template_url': 'https://github.com/Buuntu/fastapi-react',
            'template_description': 'A cookiecutter template for bootstrapping a FastAPI and React project using a modern stack.',
            'template_tags': ['Python', 'FastAPI','React', 'PostgreSQL','SQLAlchemy','Pytest','Prettier','ESlint', 'MaterialUI'],
            'recommended_by': ['FastAPI', 'React', 'Authentication', 'Frontend', 'Full-Stack'],
            'template_tree':""
        },
    {'created_by': admin_id,
     'is_private': is_private,
        'template_name': 'Cookiecutter Pylibrary',
        'template_url': 'https://github.com/ionelmc/cookiecutter-pylibrary',
        'template_description': 'Enhanced template for Python libraries',
        'template_tags': ['Python', 'Library', 'TravisCI', 'AppVeyor', 'Codecov', 'Coveralls', 'Sphinx'],
        'recommended_by': ['Library', 'Python'],
            'template_tree':""
    },
    {'created_by': admin_id,
     'is_private': is_private,
        'template_name': 'Cookiecutter Pypackage',
        'template_url': 'https://github.com/audreyfeldroy/cookiecutter-pypackage',
        'template_description': 'A Python package template',
        'template_tags': ['Python', 'Package', 'TravisCI', 'Sphinx'],
        'recommended_by': ['Package', 'Python'],
            'template_tree':""
    },
    {'created_by': admin_id,
     'is_private': is_private,
        'template_name': 'Cookiecutter Pytest Plugin',
        'template_url': 'https://github.com/pytest-dev/cookiecutter-pytest-plugin',
        'template_description': 'Minimal template for authoring pytest plugins that help you to write better programs',
        'template_tags': ['Python', 'Pytest', 'Plugin'],
        'recommended_by': ['Pytest', 'Python'],
            'template_tree':""
    },
    {'created_by': admin_id,
     'is_private': is_private,
        'template_name': 'Hatch',
        'template_url': 'https://github.com/pypa/hatch',
        'template_description': 'A modern project, package, and virtual environment manager for Python',
        'template_tags': ['Python', 'Project Management', 'Virtual Environment'],
        'recommended_by': ['Hatch', 'Python', 'Virtual Environment', 'Project Management'],
            'template_tree':""
    },
    {'created_by': admin_id,
     'is_private': is_private,
        'template_name': 'Python Package Template',
        'template_url': 'https://github.com/TezRomacH/python-package-template',
        'template_description': 'Project structure for your next Python package with state-of-the-art libraries and best development practices',
        'template_tags': ['Python', 'Package', 'Best Practices', 'Github Actions', 'Black'],
        'recommended_by': ['Best Practices', 'Python', 'Package'],
            'template_tree':""
    },
    {'created_by': admin_id,
     'is_private': is_private,
        'template_name': 'Template Python',
        'template_url': 'https://github.com/jacebrowning/template-python',
        'template_description': 'A template for new Python libraries',
        'template_tags': ['Python', 'Library'],
        'recommended_by': ['Python', 'Library'],
            'template_tree':""
    }
    ]