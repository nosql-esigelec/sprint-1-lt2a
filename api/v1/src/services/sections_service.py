"""
This module contains the SectionService class which is responsible for managing Section operations.
It includes methods to get sections and expose them, retrieve a section given a node property value, and get the next section.
It also includes methods to get questions for a section and get the next questions given a question ID and option text.
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
        """
        Retrieves a list of sections from the database.

        Returns:
            list: A list of sections.
        """
        sections = self.neo4j.read(
            tx_type="node",
            node_label="Section",
            properties={},
            many=True,
            sort=["order", "ASC"],
        ).get("result")
        return sections

    def get_section_by_property(self, property: str, value: str) -> dict:
        """
        Retrieves a section from the database based on the specified property and value.

        Args:
            property (str): The property to search for.
            value (str): The value to match.

        Returns:
            dict: The section matching the specified property and value.
        """
        section = self.neo4j.read(
            tx_type="node",
            node_label="Section",
            properties={property: value},
            many=False,
        ).get("result")
        return section

    def get_next_section(self, section_id: str) -> dict:
        """
        Get the next section.

        Args:
            section_id (str): The section ID.

        Returns:
            dict: The next section.
        """

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
        """
        Retrieves the questions associated with a given section.

        Args:
            section_id (str): The ID of the section.

        Returns:
            list: A list of dictionaries representing the questions.
        """
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

        questions_processed.reverse()
        return questions_processed

    def get_next_questions(self, question_id: str, option_text: str) -> list:
        """
        Retrieves the next set of questions based on the given question ID and option text.

        Args:
            question_id (str): The ID of the current question.
            option_text (str): The text of the selected option.

        Returns:
            list: A list of dictionaries representing the next questions and their options.
        """
        questions = self.neo4j.read(
            tx_type="relationship",
            start_node_label="Option",
            start_node_properties={"text": option_text, "question_id": question_id},
            end_node_label="Question",
            end_node_properties={},
            relation_type="LEADS_TO",
            many=True,
        ).get("result")

        # Extract the properties of the end node (which represents the question)
        extracted_questions = [question["end"] for question in questions]
        # Get the options for each question
        questions_processed = []
        for question in extracted_questions:
            question_dict = dict(question.items())
            options = self.neo4j.read(
                tx_type="relationship",
                start_node_label="Question",
                start_node_properties=question_dict,
                end_node_label="Option",
                end_node_properties={},
                relation_type="HAS_OPTION",
                many=True,
            ).get("result")
            extracted_options = [option["end"] for option in options]
            extracted_options.reverse()
            question_dict["options"] = extracted_options
            questions_processed.append(question_dict)
        return questions_processed