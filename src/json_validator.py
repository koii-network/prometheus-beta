import json

def is_valid_json(input_string: str) -> bool:
    """
    Check if the given string is a valid JSON.

    Args:
        input_string (str): The string to validate as JSON.

    Returns:
        bool: True if the string is valid JSON, False otherwise.

    Examples:
        >>> is_valid_json('{"name": "John", "age": 30}')
        True
        >>> is_valid_json('{"invalid": json')
        False
    """
    try:
        # Attempt to parse the string as JSON
        json.loads(input_string)
        return True
    except (json.JSONDecodeError, TypeError):
        # Return False for any JSON parsing errors or invalid input types
        return False