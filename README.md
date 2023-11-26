<div align="center">


[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/el-tegy/pycounts_ja2327072339/pycounts_ja2327072339/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/el-tegy/pycounts_ja2327072339/pycounts_ja2327072339/blob/master/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/el-tegy/pycounts_ja2327072339/pycounts_ja2327072339/releases)
[![License](https://img.shields.io/github/license/el-tegy/pycounts_ja2327072339)](https://github.com/nosql-esigelec/sprint-1-lt2a/blob/main/LICENSE)
![Coverage Report](api/v1/assets/images/coverage.svg)


![Team members](api/v1/assets/images/team_members.svg)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com) 
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-by-developers.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/uses-brains.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-with-swag.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/uses-badges.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/no-ragrets.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/not-a-bug-a-feature.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/makes-people-smile.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/it-works-why.svg)](https://forthebadge.com)
![Made with](api/v1/assets/images/made_with.svg)
[![forthebadge](https://forthebadge.com/images/badges/its-not-a-lie-if-you-believe-it.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/fixed-bugs.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/ctrl-c-ctrl-v.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/check-it-out.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/ages-18.svg)](https://forthebadge.com)

Awesome `Gocod`, where your passion for technology and your development expertise will be put to the test. 

</div>

`Gocod` is a solution designed to help developers in general to be more productive in their projects. This is achieved by exploiting knowledge bases in particular:

- Templates and project structures to get you started quickly
- Rich and exploitable error databases

This project simulated the challenges of a real working environment, where we had the opportunity to work on NoSQL databases and deploy a complete application on the GCP Cloud.

### Work plan and deliverables

- Sprint 1 **: Project Initiation, Templates, and User Management**
    - Complete CRUD functions in the back-end.
    - Implementation of MongoDB-based functionalities.
    - **Deliverables:** Source code updated on GitHub, activity reports.
- Sprint 2 **: Dynamic forms and templates recommendations**
    - Development of dynamic form questions based on the Neo4j database.
    - Integration of the template recommendation system.
    - **Deliverables:** Source code updated on GitHub, activity reports.
- Sprint 3 **: Database and Application deployment**
    - Configuring a Compute Engine instance for MongoDB.
    - Deployment of the FastAPI API and the front-end on Cloud Run.
    - **Deliverables:** Deployed cloud architecture, technical documentation, live demonstration.


### 🚀 Features

#### Development features

- Supports for `Python 3.9` and higher.
- Dependencies managed. See configuration in [`requirements.txt`](https://github.com/nosql-esigelec/sprint-1-lt2a/blob/main/api/requirements.txt).
- Code linted with [`pylint`](https://github.com/pylint-dev/pylint)
- Automatic codestyle with [`black`](https://github.com/psf/black), [`isort`](https://github.com/timothycrosley/isort) and [`pyupgrade`](https://github.com/asottile/pyupgrade).
- Ready-to-use [`pre-commit`](https://pre-commit.com/) hooks with code-formatting.
- Type checks with [`mypy`](https://mypy.readthedocs.io); docstring checks with [`darglint`](https://github.com/terrencepreilly/darglint); security checks with [`safety`](https://github.com/pyupio/safety) and [`bandit`](https://github.com/PyCQA/bandit)
- Testing with [`pytest`](https://docs.pytest.org/en/latest/).
- [`Pydantic`](https://github.com/samuelcolvin/pydantic/) – data validation and settings management using Python type hinting.
- [`FastAPI`](https://github.com/tiangolo/fastapi) is a type-driven asynchronous web framework.
- Ready-to-use [`.devcontainer`](https://github.com/nosql-esigelec/sprint-1-lt2a/tree/main/.devcontainer), and [`.gitignore`](https://github.com/nosql-esigelec/sprint-1-lt2a/blob/main/.gitignore). 

#### Deployment features

- `GitHub` integration: issue and pr templates.
- `Github Actions` with predefined [build workflow](https://github.com/nosql-esigelec/sprint-1-lt2a/blob/main/.github/workflows/classroom.yml) 
- [Terraform](https://github.com/hashicorp/terraform) for managing and provisioning cloud infrastructure.
- [Ansible](https://github.com/ansible/ansible) to make deployment and maintenance easier.
- Automatic drafts of new releases with [`Release Drafter`](https://github.com/marketplace/actions/release-drafter). Attention paid to [Semantic Versions](https://semver.org/) specification.

More specifically, our GCP infrastructure consists of: 

- A `google_compute_firewall` to define rules that allow or deny traffic to and from our virtual machine instances in a Google Compute Engine network,
- 02 `google_compute_instances` for MongoDB, 
- 02 `google_compute_instances` for Neo4J DB,
- A `google_compute_disk` (external storage) for each of our VMs : which is a persistent disk resource in Google Cloud making us able to persist data beyond the life of an instance (unlike ephemeral storage which is deleted when an instance is terminated),
- A `google_compute_attached_disk` to attach each compute disk to the dedicated compute instance.


#### How to access to our work ?

- First, make sure you have the latest version of our project: 
```bash
git clone https://github.com/nosql-esigelec/sprint-1-lt2a
```


- Then have to ask access to the Mongo and Neo4j databases to the team members by mailing `eliseetegue@gmail.com` for example. 

- Once you have been granted access, you'll probably want to see databases data. To do that, you have to :
  - Download [MongoDB Compass](https://downloads.mongodb.com/compass/mongodb-compass-1.40.4-win32-x64.exe) and install it locally,
  - Download [Neo4j Desktop](https://neo4j.com/download/) and install it locally. 

- Create new remote connection in MongoDB Compass and Neo4j Desktop using those URIs and the credentials given by this project team members ONLY 
  - MongoDB: `mongodb://<your_username>:<your_password>@34.76.255.124:27017/?retryWrites=true&w=majority`
  - Neo4j : `bolt://35.205.122.100:7687`

**WARNING:** before connecting to the databases instances, make sure the GCP VM instances are up and running.

### 📈 Releases

You can see the list of available releases on the [GitHub Releases](https://github.com/nosql-esigelec/sprint-1-lt2a/releases) page.

We follow [Semantic Versions](https://semver.org/) specification.

We use [`Release Drafter`](https://github.com/marketplace/actions/release-drafter). As pull requests are merged, a draft release is kept up-to-date listing the changes, ready to publish when you’re ready. With the categories option, you can categorize pull requests in release notes using labels.

#### List of labels and corresponding titles

|               **Label**               |  **Title in Releases**  |
| :-----------------------------------: | :---------------------: |
|       `enhancement`, `feature`        |       🚀 Features       |
| `bug`, `refactoring`, `bugfix`, `fix` | 🔧 Fixes & Refactoring  |
|       `build`, `ci`, `testing`        | 📦 Build System & CI/CD |
|              `breaking`               |   💥 Breaking Changes   |
|            `documentation`            |    📝 Documentation     |
|            `dependencies`             | ⬆️ Dependencies updates |


### 🛡 License

[![License](https://img.shields.io/github/license/el-tegy/pycounts_ja2327072339)](https://github.com/nosql-esigelec/sprint-1-lt2a/blob/main/LICENSE)

This project is licensed under the terms of the `MIT` license.