import pytest
from api.v1.src.dependencies import get_neo4j_db


@pytest.fixture(scope="module")
def neo4j_db_instance():
    neo4j_db = get_neo4j_db()
    yield neo4j_db
    neo4j_db.close()


test_node_label_1 = "Person"
test_node_properties_1 = {"id": "test_node_1", "name": "Bob"}
test_node_label_2 = "Person"
test_node_properties_2 = {"id": "test_node_2", "name": "Alice"}
test_relationship_type = "KNOWS"
test_relationship_properties = {"since": "2023"}
test_relationship_properties_2 = {"since": "2024"}


@pytest.mark.crud_neo4j
def test_create_node(neo4j_db_instance):
    result = neo4j_db_instance.create(
        tx_type="node",
        node_label=test_node_label_1,
        properties=test_node_properties_1,
        identifier="name",
    ).get("result")

    record = result[0]
    record_dict = dict(record)
    assert result is not None
    assert record_dict.get("name") == test_node_properties_1.get("name")
    assert record_dict.get("value") == test_node_properties_1.get("value")


@pytest.mark.crud_neo4j
def test_read_node(neo4j_db_instance):
    result = neo4j_db_instance.read(
        tx_type="node",
        node_label=test_node_label_1,
        properties=test_node_properties_1,
        many=False,
    ).get("result")
    assert isinstance(result, dict)
    assert result["name"] == test_node_properties_1["name"]

@pytest.mark.crud_neo4j
def test_update_node(neo4j_db_instance):
    match_properties = {"name": "Bob"}
    neo4j_db_instance.create(
        tx_type="node",
        node_label=test_node_label_1,
        properties=test_node_properties_1,
        identifier="name",
    ).get("result")
    set_properties = {"value": 456}
    result = neo4j_db_instance.update(
        tx_type="node",
        node_label=test_node_label_1,
        match_properties=match_properties,
        set_properties=set_properties
    ).get("result")
    record = result[0]
    assert record is not None
    assert record["a"]["value"] == set_properties["value"]
    assert record["a"]["name"] == match_properties["name"]
    assert record["a"]["id"] == test_node_properties_1["id"]

@pytest.mark.crud_neo4j
def test_delete_node(neo4j_db_instance):
    result = neo4j_db_instance.delete(
        tx_type="node", node_label=test_node_label_1, properties=test_node_properties_1
    ).get("result")
    assert result is not None
    # since result is a dict, we have to access its items using brackets
    assert result.get("_contains_updates") == True
    assert result.get("nodes_deleted") == 1


@pytest.mark.crud_neo4j
def test_create_relationship(neo4j_db_instance):
    # Create start and end nodes first
    neo4j_db_instance.create(
        tx_type="node",
        node_label=test_node_label_1,
        properties=test_node_properties_1,
        identifier="name",
    )
    neo4j_db_instance.create(
        tx_type="node",
        node_label=test_node_label_2,
        properties=test_node_properties_2,
        identifier="name",
    )

    result = neo4j_db_instance.create(
        tx_type="relationship",
        start_node_label=test_node_label_1,
        start_node_properties=test_node_properties_1,
        end_node_label=test_node_label_2,
        end_node_properties=test_node_properties_2,
        relation_type=test_relationship_type,
    ).get("result")

    assert result is not None
    assert result[0]["name"] == test_node_properties_1["name"]
    assert result[1] == test_relationship_type
    assert result[2]["name"] == test_node_properties_2["name"]


@pytest.mark.crud_neo4j
def test_read_relationship(neo4j_db_instance):
    result = neo4j_db_instance.read(
        tx_type="relationship",
        start_node_label=test_node_label_1,
        start_node_properties=test_node_properties_1,
        end_node_label=test_node_label_2,
        end_node_properties=test_node_properties_2,
        relation_type=test_relationship_type,
    ).get("result")

    assert result is not None
    assert result[0]["name"] == test_node_properties_1["name"]
    assert result[1] == test_relationship_type
    assert result[2]["name"] == test_node_properties_2["name"]


@pytest.mark.crud_neo4j
def test_update_relationship(neo4j_db_instance):
    new_properties = {"since": "2023"}

    result = neo4j_db_instance.update(
        tx_type="relationship",
        start_node_label=test_node_label_1,
        start_node_properties=test_node_properties_1,
        end_node_label=test_node_label_2,
        end_node_properties=test_node_properties_2,
        relation_type=test_relationship_type,
        new_properties=new_properties,
    ).get("result")

    assert result is not None
    assert result._contains_updates == True
    assert result.properties_set == 1


@pytest.mark.crud_neo4j
def test_delete_relationship(neo4j_db_instance):
    result = neo4j_db_instance.delete(
        tx_type="relationship",
        start_node_label=test_node_label_1,
        start_node_properties=test_node_properties_1,
        end_node_label=test_node_label_2,
        end_node_properties=test_node_properties_2,
        relation_type=test_relationship_type,
    ).get("result")

    assert result is not None
    assert result._contains_updates == True
    assert result.relationships_deleted == 1