from datetime import datetime

def convert_timestamp_to_human_readable(timestamp):
    """
    Convert a timestamp to a human-readable date string.
    
    Args:
        timestamp (int or float): Unix timestamp (seconds since epoch)
    
    Returns:
        str: Human-readable date string in the format 'Month Day, Year'
    
    Raises:
        TypeError: If timestamp is not a number
        ValueError: If timestamp is negative
    """
    # Validate input
    if not isinstance(timestamp, (int, float)):
        raise TypeError("Timestamp must be a number")
    
    if timestamp < 0:
        raise ValueError("Timestamp cannot be negative")
    
    # Convert timestamp to datetime object
    try:
        date_obj = datetime.fromtimestamp(timestamp)
        return date_obj.strftime("%B %d, %Y")
    except (ValueError, OSError):
        raise ValueError("Invalid timestamp: unable to convert to date")