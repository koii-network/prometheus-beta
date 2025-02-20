def get_unique_sorted_chars(input_string):
    """
    Takes a string and returns a sorted list of unique characters in case-sensitive alphabetical order.
    
    Args:
        input_string (str): The input string to process
    
    Returns:
        list: A sorted list of unique characters from the input string
    """
    # Handle None or empty string inputs
    if input_string is None:
        return []
    
    # Convert string to list of unique characters and sort them
    unique_chars = sorted(set(input_string))
    
    return unique_chars