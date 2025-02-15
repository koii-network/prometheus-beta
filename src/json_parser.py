import json
from typing import Dict, Any, Optional

def parse_api_response(response: str) -> Optional[Dict[Any, Any]]:
    """
    Parse a JSON response from an API.
    
    Args:
        response (str): A JSON-formatted string response from an API.
    
    Returns:
        Optional[Dict[Any, Any]]: A dictionary containing the parsed JSON data,
        or None if parsing fails.
    
    Raises:
        json.JSONDecodeError: If the input is not a valid JSON string.
    """
    try:
        # Attempt to parse the JSON string into a dictionary
        parsed_data = json.loads(response)
        return parsed_data
    except json.JSONDecodeError:
        # Return None if JSON parsing fails
        return None