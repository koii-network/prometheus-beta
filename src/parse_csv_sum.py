def parse_csv_sum(csv_string):
    """
    Parse a comma-separated string of numbers and return their sum.
    
    Args:
        csv_string (str): A string of comma-separated integers
    
    Returns:
        int: The sum of all numbers in the string
    
    Raises:
        ValueError: If the input is not a valid comma-separated string of integers
    """
    # Handle empty string case
    if not csv_string:
        return 0
    
    try:
        # Split the string and convert each element to an integer
        numbers = [int(num.strip()) for num in csv_string.split(',')]
        
        # Return the sum of the numbers
        return sum(numbers)
    except (ValueError, TypeError):
        # Raise an error if any conversion fails
        raise ValueError("Input must be a valid comma-separated string of integers")