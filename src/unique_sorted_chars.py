def get_unique_sorted_chars(input_string):
    """
    Returns a sorted list of unique characters from the input string.
    
    Args:
        input_string (str): The input string to process.
    
    Returns:
        list: A sorted list of unique characters in case-sensitive alphabetical order.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Use a sorted list comprehension to get unique characters in case-sensitive order
    return sorted(list(set(input_string)))