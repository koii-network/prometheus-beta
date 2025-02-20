def calculate_number_range_diff(number_string):
    """
    Calculate the difference between the largest and smallest numbers 
    in a comma-separated string of integers.
    
    Args:
        number_string (str): A string of comma-separated integers
    
    Returns:
        int: The difference between the largest and smallest numbers
    
    Raises:
        ValueError: If the input string is empty or contains non-integer values
    """
    # Check if the string is empty or contains only whitespace
    if not number_string or number_string.isspace():
        raise ValueError("Input string cannot be empty")
    
    # Remove any whitespace and split the string
    try:
        numbers = [int(num.strip()) for num in number_string.split(',')]
    except ValueError:
        raise ValueError("Input must be a comma-separated string of integers")
    
    # Calculate and return the difference between max and min
    return max(numbers) - min(numbers)