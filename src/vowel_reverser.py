def reverse_vowels_in_substring(s: str, start: int, end: int) -> str:
    """
    Reverse the vowels in a specified substring of a given string.
    
    Args:
        s (str): The input string.
        start (int): The starting index of the substring (inclusive).
        end (int): The ending index of the substring (exclusive).
    
    Returns:
        str: A new string with vowels in the specified substring reversed.
    
    Raises:
        ValueError: If start or end indices are out of bounds.
    """
    # Validate input indices
    if start < 0 or end > len(s) or start >= end:
        raise ValueError("Invalid substring indices")
    
    # Define vowels (both lowercase and uppercase)
    vowels = set('aeiouAEIOU')
    
    # Convert string to list for easier manipulation
    chars = list(s)
    
    # Extract positions and values of vowels in the substring
    vowel_positions = []
    vowel_chars = []
    for i in range(start, end):
        if chars[i] in vowels:
            vowel_positions.append(i)
            vowel_chars.append(chars[i])
    
    # Reverse the list of vowel characters
    vowel_chars = vowel_chars[::-1]
    
    # Replace vowels in their original positions with reversed characters
    for pos, char in zip(vowel_positions, vowel_chars):
        chars[pos] = char
    
    return ''.join(chars)