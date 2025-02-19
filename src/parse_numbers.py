def sum_comma_separated_numbers(number_string: str) -> int:
    """
    Parse a comma-separated string of numbers and return their sum.
    
    Args:
        number_string (str): A string of comma-separated integers
    
    Returns:
        int: The sum of all numbers in the string
    
    Raises:
        ValueError: If the input string contains non-integer values
    """
    # If the string is empty, return 0
    if not number_string:
        return 0
    
    # Split the string by commas and convert to integers
    try:
        numbers = [int(num.strip()) for num in number_string.split(',')]
    except ValueError:
        raise ValueError("Input string must contain only integers separated by commas")
    
    # Return the sum of numbers
    return sum(numbers)