import json
from typing import Any, Dict, Optional, Union

def parse_api_response(response: Union[str, bytes, Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    """
    Parse a JSON response from an API.

    Args:
        response (Union[str, bytes, Dict[str, Any]]): The API response to parse.
            Can be a JSON string, bytes, or already parsed dictionary.

    Returns:
        Optional[Dict[str, Any]]: Parsed JSON response as a dictionary, 
        or None if parsing fails.

    Raises:
        TypeError: If the input is not a string, bytes, or dictionary.
        json.JSONDecodeError: If the input is an invalid JSON string.
    """
    # If already a dictionary, return as-is
    if isinstance(response, dict):
        return response

    # If input is bytes, decode to string
    if isinstance(response, bytes):
        try:
            response = response.decode('utf-8')
        except UnicodeDecodeError:
            return None

    # If input is a string, parse JSON
    if isinstance(response, str):
        # Remove leading/trailing whitespace
        response = response.strip()
        
        # Handle empty string
        if not response:
            return None

        try:
            return json.loads(response)
        except json.JSONDecodeError:
            return None

    # If we get here, it's an unsupported type
    raise TypeError(f"Unsupported response type: {type(response)}")