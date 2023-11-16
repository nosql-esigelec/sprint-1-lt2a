"""
Section Service
"""
# pylint: disable=W0212
from api.v1.src.db.neo4j_db import Neo4jDB


class SectionService:
    """
    Class to manage project operations.
    """

    def __init__(self, neo4j: Neo4jDB = None):
        self.neo4j = neo4j

    def get_options_for_question(self, question_id: str) -> list:
        """
        Get options for a question.

        Args:
            question_id (str): The question ID.

        Returns:
            List[dict]: The options.
        """
        # hint: This method can inspire you to implement some with relationships.
        options = self.neo4j.read(
            tx_type="relationship",
            start_node_label="Question",
            start_node_properties={"id": question_id},
            end_node_label="Option",
            end_node_properties={},
            relation_type="HAS_OPTION",
            many=True,
        ).get("result")
        # the key 2 is the right part of the relationship where 0 is the left part and 1 is the relationship
        options = [option[2] for option in options]
        return options

    def get_sections(self) -> list:
        sections = self.neo4j.read(
            tx_type="node",
            node_label="Section",
            properties={},
            many=True,
            sort=["order", "ASC"],
        ).get("result")
        return sections

    def get_section_by_property(self, property: str, value: str) -> dict:
        section = self.neo4j.read(
            tx_type="node",
            node_label="Section",
            properties={property: value},
            many=False,
        ).get("result")
        return section

        return section

    def get_next_section(self, section_id: str) -> dict:
        """
        Get the next section.

        Args:
            section_id (str): The section ID.

        Returns:
            dict: The next section.
        """
        # TODO(neo4j): Get Next Section
        # Implement this method to get the next section.
        # (fixme, neo4j): Build a Cypher query to get the next node of Label Section.
        # The next section has an order that is greater than the order of the current section.
        # You can use the `read` method of the Neo4jDB class to get a node of Label Section by a specific property.

        # Find the current section
        current_section = self.neo4j.read(
            tx_type="node",
            node_label="Section",
            properties={"id": section_id},
            many=False,
        ).get("result")
        # Get the order of the current section
        current_section_order = current_section["order"]
        # Get the next section order
        next_section_order = current_section_order + 1
        # Get the next section
        next_section = self.neo4j.read(
            tx_type="node",
            node_label="Section",
            properties={"order": next_section_order},
            many=False,
        ).get("result")
        return next_section

    def get_questions_for_section(self, section_id: str) -> list:
        # Find the questions for the section
        start_node_property = {"id": section_id}
        result = self.neo4j.read(
            tx_type="relationship",
            start_node_label="Section",
            start_node_properties=start_node_property,
            end_node_label="Question",
            end_node_properties={},
            relation_type="HAS_QUESTION",
            many=True,
        ).get("result")
        
        questions = result
        # Get the options for each question
        questions_processed = []
        for question in questions:
            question_dict = dict(question["end"].items())
            questions_processed.append(question_dict)
        
        return questions_processed

    def get_next_questions(self, question_id: str, option_text: str) -> list:
        questions = self.neo4j.read(
            tx_type="relationship",
            start_node_label="Option",
            start_node_properties={"text": option_text, "question_id": question_id},
            end_node_label="Question",
            end_node_properties={},
            relation_type="LEADS_TO",
            many=True,
        ).get("result")
        return questions
