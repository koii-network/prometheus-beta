import sys

def log_with_size(message, size='medium'):
    """
    Log output with different font sizes.
    
    Args:
        message (str): The message to log
        size (str, optional): Font size. 
            Supports 'small', 'medium', 'large', 'xlarge'. 
            Defaults to 'medium'.
    
    Raises:
        ValueError: If an invalid size is provided
    """
    # Define size mappings (using ANSI escape codes)
    size_mapping = {
        'small': '\033[2m',     # Dim/Small text
        'medium': '\033[0m',    # Normal text
        'large': '\033[1m',     # Bold/Large text
        'xlarge': '\033[1m\033[4m'  # Bold and Underline for extra large
    }
    
    # Validate size
    if size not in size_mapping:
        raise ValueError(f"Invalid size. Choose from {list(size_mapping.keys())}")
    
    # Apply size formatting and print
    try:
        print(f"{size_mapping[size]}{message}\033[0m")
    except Exception as e:
        print(f"Error logging message: {e}", file=sys.stderr)