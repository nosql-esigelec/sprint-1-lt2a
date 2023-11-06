from typing import List, Union, Dict



def parse_mongo_id(
    data: Union[dict, list], document_type: str = "project", keep_id: bool = False
) -> Union[Dict, List[Dict]]:
    """
    Parse the mongo ID to the document ID.
    
    Args:
        data (Union[dict, list]): The data to be parsed.
        document_type (str, optional): The document type. Defaults to "project".
        
    Returns:
        Union[Dict, List[Dict]]: The parsed data.
    """
    suffix = document_type[0]
    if isinstance(data, list):
        data_list = []
        for item in data:
            item[f"{suffix}id"] = str(item["_id"])
            item["_id"] = str(item["_id"])
            if not keep_id:
                del item["_id"]
            data_list.append(item)
        return data_list
    else:
        data[f"{suffix}id"] = str(data["_id"])
        data["_id"] = str(data["_id"])
        if not keep_id:  
            del data["_id"]
        return data

def format_dict_for_cypher(d: dict) -> str:
    return '{' + ', '.join(f"{k}: '{v}'" for k, v in d.items()) + '}'