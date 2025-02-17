import json
from typing import Dict, Any, Optional

def parse_api_response(response: str) -> Optional[Dict[Any, Any]]:
    """
    Parse a JSON response from an API.
    
    Args:
        response (str): A JSON-formatted string from an API response.
    
    Returns:
        Optional[Dict[Any, Any]]: A dictionary containing the parsed JSON data,
        or None if parsing fails.
    
    Raises:
        ValueError: If the input is not a valid JSON string.
    """
    if not response or not isinstance(response, str):
        return None
    
    try:
        # Parse the JSON string into a Python dictionary
        parsed_data = json.loads(response)
        return parsed_data
    except json.JSONDecodeError as e:
        # Raise a more informative error if JSON is invalid
        raise ValueError(f"Invalid JSON format: {str(e)}")