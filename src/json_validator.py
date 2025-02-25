import json

def is_valid_json(input_string: str) -> bool:
    """
    Check if the given string is a valid JSON.

    Args:
        input_string (str): The string to validate as JSON.

    Returns:
        bool: True if the string is valid JSON, False otherwise.
    """
    try:
        # Attempt to parse the string as JSON
        json.loads(input_string)
        return True
    except (json.JSONDecodeError, TypeError):
        # Return False if parsing fails due to invalid JSON or non-string input
        return False