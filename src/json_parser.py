import json
from typing import Any, Dict, Optional

def parse_api_response(response: str) -> Optional[Dict[str, Any]]:
    """
    Parse a JSON response from an API.
    
    Args:
        response (str): A JSON-formatted string response from an API.
    
    Returns:
        Optional[Dict[str, Any]]: A dictionary containing the parsed JSON data,
        or None if parsing fails.
    
    Raises:
        ValueError: If the input is not a valid JSON string.
    """
    try:
        # Attempt to parse the JSON string
        parsed_data = json.loads(response)
        
        # Validate that the parsed data is a dictionary
        if not isinstance(parsed_data, dict):
            raise ValueError("Parsed JSON must be a dictionary")
        
        return parsed_data
    
    except json.JSONDecodeError:
        # Handle invalid JSON string
        raise ValueError("Invalid JSON string")
    except Exception as e:
        # Catch any other unexpected errors
        raise ValueError(f"Error parsing JSON: {str(e)}")