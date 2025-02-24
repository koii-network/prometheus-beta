import sys

def log_error(message: str) -> None:
    """
    Log an error message to the console's standard error stream.

    Args:
        message (str): The error message to be logged.

    Raises:
        TypeError: If the message is not a string.
    """
    # Validate input type
    if not isinstance(message, str):
        raise TypeError("Error message must be a string")
    
    # Log the error message to stderr
    print(f"ERROR: {message}", file=sys.stderr)