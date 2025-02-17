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
        # Special handling for unsupported types
        def default_serializer(o):
            return f"<Unserializable {type(o).__name__} object>"
        
        # Custom function to truncate deep nested structures
        def truncate_deep_dict(d, depth=0):
            if depth >= max_depth:
                return "..." if isinstance(d, dict) else d
            
            if isinstance(d, dict):
                return {k: truncate_deep_dict(v, depth+1) for k, v in d.items()}
            elif isinstance(d, list):
                return [truncate_deep_dict(v, depth+1) for v in d]
            return d
        
        # Truncate deep structures before serialization
        truncated_obj = truncate_deep_dict(obj)
        
        # Try to use JSON first with custom serialization
        try:
            return json.dumps(truncated_obj, indent=indent, default=default_serializer)
        except TypeError:
            # Fallback to pprint with custom representation
            pp = pprint.PrettyPrinter(indent=indent, depth=max_depth)
            return pp.pformat(truncated_obj)
    
    except Exception as e:
        # Last resort error handling
        return f"Unable to log object: {str(e)}\nObject type: {type(obj)}"