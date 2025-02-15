import json
from typing import Dict, Any, Optional

def parse_json_response(response: str) -> Optional[Dict[Any, Any]]:
    """
    Parse a JSON response from an API.
    
    Args:
        response (str): A JSON-formatted string response from an API.
    
    Returns:
        Optional[Dict[Any, Any]]: A dictionary containing the parsed JSON data,
                                  or None if parsing fails.
    
    Raises:
        ValueError: If the input is not a valid JSON string.
    """
    try:
        # Attempt to parse the JSON string
        parsed_response = json.loads(response)
        return parsed_response
    except json.JSONDecodeError as e:
        # If JSON parsing fails, raise a ValueError with details
        raise ValueError(f"Invalid JSON format: {str(e)}")