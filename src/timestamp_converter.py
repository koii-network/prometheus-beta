from datetime import datetime

def timestamp_to_human_readable(timestamp):
    """
    Convert a timestamp to a human-readable date string.

    Args:
        timestamp (int or float): A Unix timestamp representing seconds since the epoch.

    Returns:
        str: A human-readable date string in the format 'YYYY-MM-DD HH:MM:SS'.

    Raises:
        TypeError: If the input is not a number (int or float).
        ValueError: If the timestamp is negative or cannot be converted.
    """
    # Type checking
    if not isinstance(timestamp, (int, float)):
        raise TypeError("Timestamp must be a number (int or float)")
    
    # Validate timestamp range
    if timestamp < 0:
        raise ValueError("Timestamp cannot be negative")
    
    try:
        # Convert timestamp to datetime and format
        return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    except (ValueError, OverflowError):
        raise ValueError("Invalid timestamp: Unable to convert to date")