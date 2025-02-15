from datetime import datetime

def calculate_timestamp_difference(timestamp1, timestamp2, format='%Y-%m-%d %H:%M:%S'):
    """
    Calculate the time difference between two timestamps.
    
    Args:
        timestamp1 (str): First timestamp as a string.
        timestamp2 (str): Second timestamp as a string.
        format (str, optional): Format of the timestamps. Defaults to '%Y-%m-%d %H:%M:%S'.
    
    Returns:
        dict: A dictionary containing the time difference in various units.
    
    Raises:
        ValueError: If timestamps cannot be parsed or are in invalid format.
    """
    try:
        # Convert string timestamps to datetime objects
        dt1 = datetime.strptime(timestamp1, format)
        dt2 = datetime.strptime(timestamp2, format)
        
        # Calculate the absolute time difference
        time_diff = abs(dt2 - dt1)
        
        # Extract difference components
        days = time_diff.days
        hours, remainder = divmod(time_diff.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        total_seconds = int(time_diff.total_seconds())
        
        return {
            'days': days,
            'hours': hours,
            'minutes': minutes,
            'seconds': seconds,
            'total_seconds': total_seconds
        }
    except ValueError as e:
        raise ValueError(f"Invalid timestamp format: {e}")