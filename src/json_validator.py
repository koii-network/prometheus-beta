import json

def is_valid_json(json_string):
    """
    Check if a given string is a valid JSON.
    
    Args:
        json_string (str): The string to validate as JSON.
    
    Returns:
        bool: True if the string is valid JSON, False otherwise.
    """
    try:
        json.loads(json_string)
        return True
    except (json.JSONDecodeError, TypeError):
        return False