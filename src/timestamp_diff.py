from datetime import datetime

def calculate_timestamp_difference(timestamp1, timestamp2, format='%Y-%m-%d %H:%M:%S'):
    """
    Calculate the time difference between two timestamps.
    
    Args:
        timestamp1 (str): First timestamp string
        timestamp2 (str): Second timestamp string
        format (str, optional): Timestamp format. Defaults to '%Y-%m-%d %H:%M:%S'
    
    Returns:
        dict: A dictionary containing time difference in various units
    
    Raises:
        ValueError: If timestamps cannot be parsed or are in incorrect format
    """
    try:
        # Parse timestamps using the specified format
        dt1 = datetime.strptime(timestamp1, format)
        dt2 = datetime.strptime(timestamp2, format)
        
        # Calculate absolute time difference
        time_diff = abs(dt2 - dt1)
        
        # Extract different time components
        total_seconds = int(time_diff.total_seconds())
        days = time_diff.days
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        return {
            'total_seconds': total_seconds,
            'days': days,
            'hours': hours,
            'minutes': minutes,
            'seconds': seconds
        }
    
    except ValueError as e:
        raise ValueError(f"Error parsing timestamps: {e}. Ensure timestamps match the specified format.")