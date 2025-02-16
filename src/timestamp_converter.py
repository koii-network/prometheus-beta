from datetime import datetime

def timestamp_to_human_readable_date(timestamp):
    """
    Convert a timestamp to a human-readable date string.
    
    Args:
        timestamp (int or float): Unix timestamp (seconds since epoch)
    
    Returns:
        str: Formatted date string in the format 'Month Day, Year'
    
    Raises:
        ValueError: If timestamp is not a valid number
        TypeError: If timestamp is not an int or float
    """
    # Validate input type
    if not isinstance(timestamp, (int, float)):
        raise TypeError("Timestamp must be an integer or float")
    
    try:
        # Convert timestamp to datetime and format
        date_obj = datetime.fromtimestamp(timestamp)
        return date_obj.strftime("%B %d, %Y")
    except ValueError as e:
        raise ValueError(f"Invalid timestamp: {e}")