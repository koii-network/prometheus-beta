def reverse_vowels_substring(s: str, start: int, end: int) -> str:
    """
    Reverse vowels in a specified substring of a string.
    
    Args:
        s (str): The input string
        start (int): Starting index of the substring (inclusive)
        end (int): Ending index of the substring (exclusive)
    
    Returns:
        str: A new string with vowels in the specified substring reversed
    
    Raises:
        ValueError: If start or end indices are out of bounds
    """
    # Validate input indices
    if start < 0 or end > len(s) or start >= end:
        raise ValueError("Invalid substring indices")
    
    # Define vowels
    vowels = set('aeiouAEIOU')
    
    # Convert string to list for easier manipulation
    chars = list(s)
    
    # Extract vowels from the substring
    substring_vowels = [char for char in chars[start:end] if char in vowels]
    substring_vowels.reverse()
    
    # Create a new list to store the result
    result_chars = chars.copy()
    
    # Replace vowels in the substring with reversed vowels
    vowel_index = 0
    for i in range(start, end):
        if chars[i] in vowels:
            result_chars[i] = substring_vowels[vowel_index]
            vowel_index += 1
    
    return ''.join(result_chars)