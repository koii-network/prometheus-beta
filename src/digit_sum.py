def sum_of_digits(input_string):
    """
    Calculate the sum of digits in a given string.
    
    Args:
        input_string (str): The input string to extract digits from.
    
    Returns:
        int: The sum of all digits in the string, ignoring leading zeros.
    """
    # Extract only the digits from the input string
    digits = [int(char) for char in input_string if char.isdigit()]
    
    # Return the sum of the digits
    return sum(digits)