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
    # Remove any whitespace and split the string
    try:
        numbers = [int(num.strip()) for num in number_string.split(',')]
    except ValueError:
        raise ValueError("Input must be a comma-separated string of integers")
    
    # Check if the list is empty
    if not numbers:
        raise ValueError("Input string cannot be empty")
    
    # Calculate and return the difference between max and min
    return max(numbers) - min(numbers)