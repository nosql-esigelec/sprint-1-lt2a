

# Sprint 2: Dynamic forms and templates recommendations

Welcome back to Gocod.

Today, we delve into Neo4j to handle data with string relationships. You'll be implementing Neo4j CRUD operations that will be instrumental for dynamic forms and templates recommendations.

## About Forms

Our objective is to streamline project creation by tailoring a dynamic form to the user's specific needs. The form adapts based on user responses, ensuring relevance and efficiency. For instance, selecting 'Data Science' as a project type triggers questions related to frameworks like PyTorch or TensorFlow, whereas a 'Web App' project would prompt questions about frontend frameworks such as React, Vue, or Angular.

The form comprises three elements:

**Sections**: 
A logical grouping of questions. Each subsequent section's content is influenced by the answers provided in the preceding ones.

**Questions**: A mix of statements and response fields, varying based on the field type (text, select, multiselect).

**Options**: Possible responses that guide the flow of subsequent questions.


Our Data Engineering team maintain a initial base of sections, questions and answers to fill the database with. They are working on ingestion scripts to fill the database initially. So this time, you'll consider Data Engineers as additional customers.

Before we begin, let's install the dependencies(if not already done). Run the following command in your terminal:

```bash
pip install -r api/requirements.txt
```
> Don't forget to update the `.env` file with Neo4j credentials(URI, USER and PASSWORD)

### Part 1: Neo4j Database
#### Task
Implement the CRUD operations in the Neo4j class within the file `neo4j_db.py`.

#### User Stories
- "As a developer, I want to create a Neo4j connection."
- "As a developer, I want to create new nodes and relationships in the database."
- "As a developer, I want to read nodes and relationships from the database."
- "As a developer, I want to update nodes and relationships in the database."
- "As a developer, I want to delete nodes and relationships from the database."

#### Methods to Implement
File to edit: `api/v1/src/dependencies.py`
- Create a Neo4j instance(from the class Neo4jDB) that will be reused in the other methods.

File to edit:  `api/v1/src/db/neo4j_db.py`

- `create_node`: Create a new node in the database.
- `read_node`: Read nodes in the database.
- `update_node`: Update a node in the database.
- `delete_node`: Delete nodes in the database.
- `create_relationship`: Create a new relationship in the database.
- `read_relationship`: Read relationships in the database.
- `update_relationship`: Update relationships in the database.
- `delete_relationship`: Delete relationships in the database.

#### Testing
Run the unit tests for these CRUD operations by running:

```bash
PYTHONPATH=$(pwd)/api/v1 pytest -m crud_neo4j
```

Once the tests pass, use the command below to add, commit, and push your changes with an appropriate message:

```bash
git add .
git commit -m "feat(neo4j): Add crud neo4j operations"
git push origin <your-feature-branch>
```
> You can add commits per method if you prefer.

---

### Part 2: Dynamic form

#### Subpart 1: Section Service
##### User Stories
- "As an API developer, I want to get sections and expose them."
- "As an API developer, I want to get a section given an node property value."
- "As an API developer, I want to get the next section data given the current one."
- "As an API developer, I want to get questions for a specific section."
- "As an API developer, I want to get next questions given an answer provided to specific a question."

##### Methods to Implement
File to edit: `api/v1/src/services/section_service.py`
- `get_sections`: Get all existing sections.
- `get_section_by_property`: Get a section by a property value(id, name, etc...)
- `get_next_section`: Get the next section given a section id.
- `get_questions_for_section`: Get all the questions for a specific section.
- `get_next_questions`: Get the questions that need to be asked given an option chosed.

#### Testing
Run the unit tests for these CRUD operations by running:

```bash
PYTHONPATH=$(pwd)/api/v1 pytest -m section_service
```

#### Subpart 2: Project Service
##### User Stories
- "As a user, I want to create a project with recommendations."
- "As a user, I want to completely delete my projects from the app."
- "As a user, I want to get the templates recommended given my answers."
- "As a user, I want to select a recommended template."

##### Methods to Implement
File to edit: `api/v1/src/services/project_service.py`
- `create_project`: Create a project in the Neo4j database with the provided answers as properties(for the recommendations).
- `delete_project`: Delete the project also from the Neo4j database.
- `get_recommended_templates`: Get recommendations for the project given the options chosed(properties).
- `select_template`: Select a template for project.

#### Testing
Run the unit tests for these CRUD operations by running:

```bash
PYTHONPATH=$(pwd)/api/v1 pytest -m project_service
```


#### Subpart 3: Template Service
##### User Stories
- "As a user, I want to create a new template that will recommendable."
- "As a user, I want to completely delete my templates from the app."

##### Methods to Implement
File to edit: `api/v1/src/services/template_service.py`
- `create_template`: Create a template in the Neo4j database.
- `delete_template`: Delete a template from Neo4j database given properties.

#### Testing
Run the unit tests for these CRUD operations by running:

```bash
PYTHONPATH=$(pwd)/api/v1 pytest -m template_service
```


