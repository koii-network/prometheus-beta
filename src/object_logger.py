import json
import pprint

def log_object(obj, indent=2, width=80, depth=None):
    """
    Log an object in a readable format.
    
    Args:
        obj: The object to be logged
        indent (int, optional): Number of spaces for indentation. Defaults to 2.
        width (int, optional): Maximum width of the output. Defaults to 80.
        depth (int, optional): Maximum depth of nested structures to print. Defaults to None.
    
    Returns:
        str: A formatted string representation of the object
    """
    try:
        # Try pretty printing first (works well for dictionaries, lists, etc.)
        pp = pprint.PrettyPrinter(indent=indent, width=width, depth=depth)
        formatted = pp.pformat(obj)
        return formatted
    except Exception:
        # Fallback to JSON for more generic object representation
        try:
            return json.dumps(obj, indent=indent)
        except (TypeError, ValueError):
            # If JSON serialization fails, use str representation
            return str(obj)