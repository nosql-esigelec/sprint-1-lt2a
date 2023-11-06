from functools import wraps
import logging
from pymongo import errors
import random
import string

def generate_response(success: bool, message: str, result: any = "0") -> dict:
    """
    Generate a standardized response dictionary.

    Args:
        success (bool): Whether the operation was successful.
        message (str): A message describing the outcome.
        result (any, optional): The result data, if any. Defaults to None.

    Returns:
        dict: The response dictionary.
    """
    return {"success": success, "message": message, "result": result}

def handle_db_operations(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return generate_response(True, "Operation successful", result)
        except errors.WriteError as of:
            message = f"An error occurred on write operation: {of}"
            logging.error(message)
            return generate_response(False, message)
        except errors.OperationFailure as of:
            message = f"An operation failure occurred: {of}"
            logging.error(message)
            return generate_response(False, message)
    return wrapper


def build_query_sort_project(filters):
    """
    Build the query, sort, and project parameters for a given filters object.
    
    Args:
        filters (dict): The filters to be applied.
        
    Returns:
        tuple: The query, sort, and project parameters.
    """
    query = {}
    sort = [('created_at', -1)]
    project = {}
    if "template_description" in filters.keys():
        filters["$text"] = {"$search": filters["template_description"]}
        meta = {"score": {"$meta": "textScore"}}
        sort = [("score", meta)]
        project["score"] = meta
    elif "template_tags" in filters.keys():
        filters["tags"] = {"$all": filters["template_tags"]}
    elif "stars" in filters.keys():
        filters["stars"] = {"$gte": int(filters["stars"])}
    else:
        sort = [('created_at', -1)]
    return query, sort, project

def random_string(length=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))
    def _log_activity(self, activity_type: str, status: str, user_id: str):
        """
        Log an activity to the database.

        Args:
            activity_type (str): The type of activity to be logged.
            status (str): The status of the activity.
            user_id (str): The ID of the user performing the activity.

        Returns:
            None
        """
        activity = {
            "user_id": user_id,
            "activity": activity_type,
            "status": status,
            "date": datetime.datetime.now(),
        }
        user = self.read({"_id": ObjectId(user_id)}, "activities").get("result")
        if user and user.get("log_activities", False):
            self.create(activity, "activities")