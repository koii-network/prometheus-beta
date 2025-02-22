def find_most_frequent_char(input_string: str) -> str:
    """
    Find the most frequently occurring character in a string.
    
    Args:
        input_string (str): The input string to analyze.
    
    Returns:
        str: The most frequently occurring character. 
             If multiple characters have the same highest frequency, 
             return the first one encountered.
    
    Raises:
        ValueError: If the input string is empty.
    """
    if not input_string:
        raise ValueError("Input string cannot be empty")
    
    # Count character frequencies
    char_count = {}
    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Find the character with the highest frequency
    most_frequent = max(char_count, key=char_count.get)
    
    return most_frequent