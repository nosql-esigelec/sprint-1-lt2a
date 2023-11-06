

# Sprint 1: Project Initiation, Templates, and User Management

Welcome to Gocod, an solution that aims to revolutionize project management and DevOps operations. As we embark on this workshop, remember that the code you write and the practices you implement are essential building blocks for the robust Gocod platform we are collectively creating.

Today, we delve into MongoDB to establish the foundation of our data handling capabilities. You'll be implementing CRUD operations that will be instrumental for user management, project initiation, and template handling. Your contributions will directly impact the efficiency and reliability of our system.


Before we begin, let's install the dependencies for this project. Run the following command in your terminal:

```bash
pip install -r api/requirements.txt
```
> Don't forget to ask the DevOps team for the `.env` file.

### Part 1: MongoDB Database
#### Task
Implement the CRUD operations in the MongoDB class within the file `mongo_db.py`.

#### User Stories
- "As a developer, I want to create a MongoDB connection."
- "As a developer, I want to create new documents in the database."
- "As a developer, I want to read documents from the database."
- "As a developer, I want to update documents in the database."
- "As a developer, I want to delete documents from the database."

#### Methods to Implement
File to edit: `api/v1/src/dependencies.py`
- Create a MongoDB connection that will be reused in the other methods.

File to edit:  `api/v1/src/db/mongo_db.py`

- `create`: Create a new document or many documents in the database.
- `read`: Read a document or many documents in the database.
- `update`: Update a document or many documents in the database.
- `delete`: Delete a document or many documents in the database.

#### Testing
Run the unit tests for these CRUD operations by running:

```bash
PYTHONPATH=$(pwd)/api/v1 pytest -m crud_operations
```

Once the tests pass, use the command below to add, commit, and push your changes with an appropriate message:

```bash
git add .
git commit -m "feat(mongo): Add crud operations"
git push origin <your-feature-branch>
```
> You can add commits per method if you prefer.





---

### Part 2: Project Initiation and Templates

#### Subpart 1: User Service
##### User Stories
- "As an admin, I want to create new users."
- "As an admin, I want to authenticate users."
- "As an admin, I want to read user information."

##### Methods to Implement
File to edit: `api/v1/src/services/user_service.py`
- `create_user`: Delete the field `org_name` from the data, create the user in the database, and return the `user_id`.
- `authenticate_user`: Find and authenticate the user given their username and password.
- `read_user`: Find and return the user given their id.

#### Testing
Run the unit tests for these CRUD operations by running:

```bash
PYTHONPATH=$(pwd)/api/v1 pytest -m user_service
```

#### Subpart 2: Project Service
##### User Stories
- "As a user, I want to update my projects."
- "As a user, I want to delete my projects."
- "As a user, I want to list all of my projects."

##### Methods to Implement
File to edit: `api/v1/src/services/project_service.py`
- `update_project`: Update the project given their id and the data.
- `delete_project`: Delete the project given their id.
- `list_projects`: List all the projects of the user that created them.

#### Testing
Run the unit tests for these CRUD operations by running:

```bash
PYTHONPATH=$(pwd)/api/v1 pytest -m project_service
```


#### Subpart 3: Template Service
##### User Stories
- "As a user, I want to create new templates."
- "As a user, I want to read templates."
- "As a user, I want to list all templates."
- "As a user, I want to delete templates."

##### Methods to Implement
File to edit: `api/v1/src/services/template_service.py`
- `create_template`: Create a template given the data. Manage the cases given the field `is_private`. If it's true, save it to the user collection; otherwise, save it to the template collection.
- `read_template`: Read a template given the id. If the `user_id` is given, read it from the user collection; otherwise, read it from the template collection.
- `list_templates`: List all the templates from the user collection if the `user_id` is given; otherwise, list all the templates from the template collection.
- `delete_template`: Delete a template given the id. If the `user_id` is given, delete it (pull) from the user collection; otherwise, delete it from the template collection.
- `star_template`: Mark a template as a favorite given its id and the one of the user who marked it as a favorite. 

#### Testing
Run the unit tests for these CRUD operations by running:

```bash
PYTHONPATH=$(pwd)/api/v1 pytest -m template_service
```


