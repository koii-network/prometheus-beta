import sys

def log_warning(message):
    """
    Log a warning message to the console.
    
    Args:
        message (str): The warning message to log.
    """
    print(f"WARNING: {message}", file=sys.stderr)