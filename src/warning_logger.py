import sys

def log_warning(message):
    """
    Log a warning message to the console using stderr.
    
    Args:
        message (str): The warning message to log.
    
    Raises:
        TypeError: If the message is not a string.
    """
    if not isinstance(message, str):
        raise TypeError("Warning message must be a string")
    
    print(f"WARNING: {message}", file=sys.stderr)