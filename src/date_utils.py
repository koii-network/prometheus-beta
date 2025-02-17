from datetime import datetime, timedelta

def add_days_to_date(input_date, days_to_add):
    """
    Add a specified number of days to a given date.
    
    Args:
        input_date (str or datetime): The initial date 
        days_to_add (int): Number of days to add to the date
    
    Returns:
        datetime: A new date after adding the specified number of days
    
    Raises:
        TypeError: If input_date is not a string or datetime object
        TypeError: If days_to_add is not an integer
        ValueError: If input_date is an invalid date string
    """
    # Check input types
    if not isinstance(days_to_add, int):
        raise TypeError("days_to_add must be an integer")
    
    # Handle different input date types
    if isinstance(input_date, str):
        try:
            # Try parsing with multiple common date formats
            date_formats = ['%Y-%m-%d', '%m/%d/%Y', '%d/%m/%Y', '%Y/%m/%d']
            
            for date_format in date_formats:
                try:
                    parsed_date = datetime.strptime(input_date, date_format)
                    break
                except ValueError:
                    continue
            else:
                raise ValueError(f"Unable to parse date: {input_date}")
        except Exception as e:
            raise ValueError(f"Invalid date format: {str(e)}")
    elif isinstance(input_date, datetime):
        parsed_date = input_date
    else:
        raise TypeError("input_date must be a string or datetime object")
    
    # Add days and return new date
    return parsed_date + timedelta(days=days_to_add)