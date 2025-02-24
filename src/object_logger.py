import json
import inspect
from typing import Any

def log_object(obj: Any, indent: int = 2) -> str:
    """
    Log an object in a readable, formatted string representation.

    This function attempts to convert the input object to a readable string format,
    handling different types of objects with appropriate serialization strategies.

    Args:
        obj (Any): The object to be logged
        indent (int, optional): Number of spaces for indentation in JSON-like output. 
                                Defaults to 2.

    Returns:
        str: A human-readable string representation of the object

    Raises:
        TypeError: If the object cannot be serialized
    """
    # Handle None first
    if obj is None:
        return "None"

    # Try different serialization methods based on object type
    try:
        # For dictionaries, use json.dumps with indentation
        if isinstance(obj, dict):
            return json.dumps(obj, indent=indent, default=str)
        
        # For lists, tuples, sets - convert to JSON-like format
        if isinstance(obj, (list, tuple, set)):
            return json.dumps(list(obj), indent=indent, default=str)
        
        # For custom objects, try to convert to a dictionary of attributes
        if hasattr(obj, '__dict__'):
            return json.dumps(
                {k: v for k, v in obj.__dict__.items() if not k.startswith('_')}, 
                indent=indent, 
                default=str
            )
        
        # For simple types (int, float, str, bool), convert to string
        if isinstance(obj, (int, float, str, bool)):
            return str(obj)
        
        # Fallback to string representation
        return repr(obj)
    
    except Exception as e:
        # If all else fails, provide a meaningful error
        raise TypeError(f"Unable to log object of type {type(obj)}: {str(e)}")