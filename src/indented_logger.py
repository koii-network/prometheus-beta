import sys

def log_with_indent(message, indent_level=0, file=sys.stdout):
    """
    Log a message with specified indentation.
    
    Args:
        message (str): The message to log
        indent_level (int, optional): Number of spaces to indent. Defaults to 0.
        file (file-like object, optional): Output stream. Defaults to sys.stdout.
    """
    # Create indentation based on indent_level
    indent = " " * (4 * indent_level)
    
    # Print the indented message
    print(f"{indent}{message}", file=file)