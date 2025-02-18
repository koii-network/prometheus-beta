import json

def is_valid_json(string):
    """
    Check if a given string is a valid JSON.
    
    Args:
        string (str): The string to validate as JSON
    
    Returns:
        bool: True if the string is valid JSON, False otherwise
    """
    try:
        json.loads(string)
        return True
    except (json.JSONDecodeError, TypeError):
        return False