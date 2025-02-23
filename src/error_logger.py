import sys

def log_error(message):
    """
    Log an error message to the console's standard error stream.

    Args:
        message (str): The error message to be logged.

    Raises:
        TypeError: If the message is not a string.
    """
    # Check if the input is a string
    if not isinstance(message, str):
        raise TypeError("Error message must be a string")
    
    # Log the error message to stderr
    print(message, file=sys.stderr)