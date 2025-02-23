import json
import pprint
import inspect

def log_object(obj, indent=2, sort_keys=False, compact=False):
    """
    Log an object in a readable format with multiple output options.

    Args:
        obj: The object to be logged (can be any JSON-serializable object)
        indent (int, optional): Number of spaces for indentation. Defaults to 2.
        sort_keys (bool, optional): Whether to sort dictionary keys. Defaults to False.
        compact (bool, optional): Use compact representation if True. Defaults to False.

    Returns:
        str: A readable string representation of the object

    Raises:
        TypeError: If the object cannot be serialized to JSON
    """
    try:
        # First, try JSON serialization for standard types
        if compact:
            return json.dumps(obj, separators=(',', ':'))
        
        return json.dumps(obj, indent=indent, sort_keys=sort_keys)
    except (TypeError, ValueError):
        # For objects that can't be directly JSON serialized
        # Try different approaches to get a readable representation
        
        # Check if object has a __dict__ attribute
        if hasattr(obj, '__dict__'):
            return pprint.pformat(obj.__dict__, indent=indent)
        
        # If no __dict__, use repr or str
        return pprint.pformat(repr(obj), indent=indent)