import json
import pprint

def log_object(obj, indent=2, max_depth=3):
    """
    Log an object in a readable, formatted manner.
    
    Args:
        obj: The object to be logged
        indent (int, optional): Number of spaces for indentation. Defaults to 2.
        max_depth (int, optional): Maximum recursion depth for nested objects. Defaults to 3.
    
    Returns:
        str: A formatted, readable string representation of the object
    """
    try:
        # Use pprint for more complex nested structures
        if max_depth > 0:
            pp = pprint.PrettyPrinter(indent=indent, depth=max_depth)
            return pp.pformat(obj)
        
        # Fallback to JSON for simpler serialization
        return json.dumps(obj, indent=indent)
    
    except (TypeError, ValueError) as e:
        # Handle objects that can't be directly serialized
        return f"Unable to log object: {str(e)}\nObject type: {type(obj)}"