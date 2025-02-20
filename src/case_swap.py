def swap_case(input_string):
    """
    Takes a single string input and returns a new string where:
    - lowercase characters are capitalized
    - uppercase characters are lowercased
    
    Args:
        input_string (str): The input string to swap case
    
    Returns:
        str: A new string with character cases swapped
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    return input_string.swapcase()