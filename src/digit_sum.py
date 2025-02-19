def sum_of_digits(input_string):
    """
    Calculate the sum of all digits in the given string.
    
    Args:
        input_string (str): The input string to extract digits from.
    
    Returns:
        int: The sum of all digits in the string, ignoring leading zeros.
    """
    # Filter out only the digits and convert to list of integers
    digits = [int(char) for char in input_string if char.isdigit()]
    
    # Return the sum of digits
    return sum(digits)