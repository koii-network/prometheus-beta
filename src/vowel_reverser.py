def reverse_vowels_in_substring(s: str, start: int, end: int) -> str:
    """
    Reverse the vowels in a substring of a given string.
    
    Args:
        s (str): The input string
        start (int): Starting index of the substring (inclusive)
        end (int): Ending index of the substring (exclusive)
    
    Returns:
        str: A new string with vowels in the specified substring reversed
    
    Raises:
        ValueError: If start or end indices are invalid
    """
    # Special case for empty string
    if s == "" and start == 0 and end == 0:
        return ""
    
    # Validate input indices
    if start < 0 or end > len(s) or start >= end:
        raise ValueError("Invalid substring indices")
    
    # Define vowels (both lowercase and uppercase)
    vowels = set('aeiouAEIOU')
    
    # Convert substring to list for easier manipulation
    chars = list(s)
    
    # Extract vowels from the substring
    substr_vowels = [char for char in chars[start:end] if char in vowels]
    
    # Reverse the vowels
    substr_vowels.reverse()
    
    # Create a new list for the result
    result_chars = chars.copy()
    
    # Replace vowels in the substring
    vowel_index = 0
    for i in range(start, end):
        if chars[i] in vowels:
            result_chars[i] = substr_vowels[vowel_index]
            vowel_index += 1
    
    return ''.join(result_chars)