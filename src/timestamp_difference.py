from datetime import datetime, timedelta

def calculate_timestamp_difference(timestamp1, timestamp2, unit='seconds'):
    """
    Calculate the time difference between two timestamps.
    
    Args:
        timestamp1 (str or datetime): First timestamp
        timestamp2 (str or datetime): Second timestamp
        unit (str, optional): Unit of time difference. 
                               Supports 'seconds', 'minutes', 'hours', 'days'. 
                               Defaults to 'seconds'.
    
    Returns:
        float: Time difference in specified unit
    
    Raises:
        ValueError: If invalid unit is provided
        TypeError: If timestamps are not datetime or valid datetime strings
    """
    # Convert string timestamps to datetime if needed
    if isinstance(timestamp1, str):
        try:
            timestamp1 = datetime.fromisoformat(timestamp1)
        except ValueError:
            raise ValueError("Invalid format for timestamp1. Use ISO format.")
    
    if isinstance(timestamp2, str):
        try:
            timestamp2 = datetime.fromisoformat(timestamp2)
        except ValueError:
            raise ValueError("Invalid format for timestamp2. Use ISO format.")
    
    # Validate input types
    if not isinstance(timestamp1, datetime) or not isinstance(timestamp2, datetime):
        raise TypeError("Timestamps must be datetime objects or ISO format strings")
    
    # Calculate time difference
    time_diff = abs(timestamp2 - timestamp1)
    
    # Convert to specified unit
    unit = unit.lower()
    if unit == 'seconds':
        return time_diff.total_seconds()
    elif unit == 'minutes':
        return time_diff.total_seconds() / 60
    elif unit == 'hours':
        return time_diff.total_seconds() / 3600
    elif unit == 'days':
        return time_diff.total_seconds() / (24 * 3600)
    else:
        raise ValueError("Invalid unit. Use 'seconds', 'minutes', 'hours', or 'days'.")