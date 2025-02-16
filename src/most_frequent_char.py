def find_most_frequent_char(s: str) -> str:
    """
    Find the most frequently occurring character in a string.
    
    If multiple characters have the same highest frequency, 
    return the character that appears first in the string.
    
    Args:
        s (str): Input string to analyze
    
    Returns:
        str: The most frequent character
    
    Raises:
        ValueError: If the input string is empty
    """
    if not s:
        raise ValueError("Input string cannot be empty")
    
    # Create a dictionary to store character frequencies
    char_freq = {}
    
    # Count character frequencies while maintaining order
    for char in s:
        if char not in char_freq:
            char_freq[char] = 1
        else:
            char_freq[char] += 1
    
    # Find the maximum frequency
    max_freq = max(char_freq.values())
    
    # Return the first character with max frequency in the original string
    return next(char for char in s if char_freq[char] == max_freq)