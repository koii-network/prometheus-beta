def find_most_frequent_char(s: str) -> str:
    """
    Find the most frequently occurring character in a string.
    
    Args:
        s (str): Input string to analyze
    
    Returns:
        str: The most frequently occurring character
    
    Raises:
        ValueError: If the input string is empty
    """
    if not s:
        raise ValueError("Input string cannot be empty")
    
    # Create a dictionary to count character frequencies
    char_counts = {}
    
    # Count occurrences of each character
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1
    
    # Find the character with the maximum frequency
    most_frequent = max(char_counts, key=char_counts.get)
    
    return most_frequent