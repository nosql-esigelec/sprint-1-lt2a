from api.v1.src.db.ingestion.data.templates import templates
from api.v1.src.db.ingestion.data.sections import sections
from api.v1.src.db.ingestion.data.questions import questions
from api.v1.src.db.ingestion.data.options import options
from api.v1.src.services.templates_service import TemplateService
from api.v1.src.dependencies import get_mongo_db, get_neo4j_db

mongo = get_mongo_db()
neo4j = get_neo4j_db()

# Instantiate the TemplateService class
#template_service = TemplateService(mongo, neo4j)
# Clear the Neo4j database
neo4j.drop()
# Clear the MongoDB collection templates
mongo.drop_collection("templates")
# Create a Mongo unique index on the `template_name` field
#mongo.create_index("templates", "template_name", unique=True)
# Create a Neo4j unique index on the `template_name` field
#neo4j.create_index("Template", "template_name")

# Create the public templates
""""
for template in templates:
    template_service.create_template(template)
    for tag in template.get('template_tags', []):
        neo4j.create(tx_type="relationship", 
                     start_node_label="Template", 
                     start_node_properties={"template_name": template.get('template_name')}, 
                     end_node_label="Tag", 
                     end_node_properties={"name": tag}, 
                     relation_type="HAS_TAG")
        neo4j.create(tx_type="relationship", 
                     start_node_label="Tag", 
                     start_node_properties={"name": tag}, 
                     end_node_label="Template", 
                     end_node_properties={"template_name": template.get("template_name")}, 
                     relation_type="RECOMMENDS")
"""

# Insert the sections
for section in sections:

    neo4j.create(
        tx_type="node",  # transaction function
        node_label="Section", # resource (node label),
        properties=section,  # unpacked section data as kwargs
        identifier="id"
    )


# Insert the questions
for question in questions:
    neo4j.create(
        tx_type="node",  # transaction function
        node_label="Question",  # identifier field
        properties={k: v for k, v in question.items() if k not in ['depends_on', 'value']},
        identifier="id"
    )
    # Create the relationships between the questions and the options that LEADS_TO them
    depends_on = question.get('depends_on', None)
    if depends_on:
        for option in question.get('value', []):
            start_node_properties = {"text": option, "question_id": depends_on}
            end_node_properties = {"id": question.get("id")}
            neo4j.create(tx_type="relationship",
                         start_node_label="Option",
                         start_node_properties=start_node_properties,
                         end_node_label="Question",
                         end_node_properties=end_node_properties,
                         relation_type="LEADS_TO")
    # Create the relationships between the sections and the questions
    neo4j.create(tx_type="relationship",
                 start_node_label="Section",
                 start_node_properties={"id": question.get("section_id")},
                 end_node_label="Question",
                 end_node_properties={"id":question.get("id")},
                 relation_type="HAS_QUESTION")
# Insert the options
for option in options:
    neo4j.create(
        tx_type="node",  # transaction function
        node_label="Option", # resource (node label),
        properties={k: v for k, v in option.items() if k not in ['applicable_languages', 'applicable_project_types']},  # unpacked section data as kwargs
        identifier="text"
    )
    # Create the relationships between the options and the tags
    for tag in option.get('tags', []):
        neo4j.create(tx_type="relationship",
                     start_node_label="Option",
                     start_node_properties={"text": option.get('text')},
                     end_node_label="Tag",
                     end_node_properties={"name": tag},
                     relation_type="HAS_TAG" )
    # Create the relationships between the options and questions
    neo4j.create(tx_type="relationship",
                 start_node_label="Question",
                 start_node_properties={"id": option.get("question_id")},
                 end_node_label="Option",
                 end_node_properties={"text": option.get("text")},
                 relation_type="HAS_OPTION" )
