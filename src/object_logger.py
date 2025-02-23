import json
import pprint

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
        # If compact is True, use minimal JSON formatting
        if compact:
            return json.dumps(obj, separators=(',', ':'))
        
        # If sort_keys is True, sort dictionary keys for consistent output
        return json.dumps(obj, indent=indent, sort_keys=sort_keys)
    except TypeError:
        # For objects that can't be directly JSON serialized, use pprint
        pp = pprint.PrettyPrinter(indent=indent)
        return pp.pformat(obj)