import json
from typing import Any, Dict, Optional

def parse_api_response(response: str) -> Optional[Dict[str, Any]]:
    """
    Parse a JSON response from an API.
    
    Args:
        response (str): A JSON-formatted string from an API response.
    
    Returns:
        Optional[Dict[str, Any]]: A dictionary containing the parsed JSON data,
        or None if parsing fails.
    
    Raises:
        json.JSONDecodeError: If the input is not a valid JSON string.
    """
    try:
        # Attempt to parse the JSON response
        parsed_data = json.loads(response)
        
        # Validate that the parsed data is a dictionary
        if not isinstance(parsed_data, dict):
            return None
        
        return parsed_data
    except json.JSONDecodeError:
        # Return None for invalid JSON
        return None