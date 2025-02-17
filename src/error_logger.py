import sys

def log_error(message):
    """
    Log an error message to the console (stderr).
    
    Args:
        message (str): The error message to log.
    
    Raises:
        TypeError: If the message is not a string.
    """
    # Validate input is a string
    if not isinstance(message, str):
        raise TypeError("Error message must be a string")
    
    # Print the error message to stderr
    print(f"ERROR: {message}", file=sys.stderr)