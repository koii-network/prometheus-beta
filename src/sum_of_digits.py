def sum_of_digits(string_input):
    """
    Calculate the sum of all digits in a given string.
    
    Args:
        string_input (str): The input string to extract digits from.
    
    Returns:
        int: The sum of all digits in the string. Leading zeros are ignored.
    """
    # Use a generator expression to extract and sum digits
    return sum(int(char) for char in string_input if char.isdigit())