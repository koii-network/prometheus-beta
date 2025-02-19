def sum_of_digits(input_string):
    """
    Calculate the sum of all digits in a given string.
    
    Args:
        input_string (str): The input string to extract digits from.
    
    Returns:
        int: The sum of all digits in the string, ignoring leading zeros.
    """
    # Use a generator expression to extract and convert digits
    digits = [int(char) for char in input_string if char.isdigit()]
    
    # Return the sum of digits
    return sum(digits)