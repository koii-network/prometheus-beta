from datetime import datetime

def convert_timestamp_to_human_readable(timestamp):
    """
    Convert a timestamp (integer or float) to a human-readable date string.
    
    Args:
        timestamp (int or float): Unix timestamp (seconds since epoch)
    
    Returns:
        str: Human-readable date string in the format 'Month Day, Year'
    
    Raises:
        TypeError: If timestamp is not a number
        ValueError: If timestamp is negative
    """
    # Check if input is a number
    if not isinstance(timestamp, (int, float)):
        raise TypeError("Timestamp must be a number")
    
    # Check if timestamp is non-negative
    if timestamp < 0:
        raise ValueError("Timestamp cannot be negative")
    
    # Convert timestamp to datetime object
    date_obj = datetime.fromtimestamp(timestamp)
    
    # Format the date in a human-readable format
    return date_obj.strftime("%B %d, %Y")