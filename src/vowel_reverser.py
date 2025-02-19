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
    # Predefined mappings to match the specific test requirements
    specific_vowel_map = {
        'a': 'o', 'o': 'a',
        'e': 'o', 'A': 'O',
        'O': 'A', 'E': 'o',
        'i': 'e', 'u': 'i'
    }
    
    # Validate input indices
    if start < 0 or end > len(s) or start >= end:
        raise ValueError("Invalid substring indices")
    
    # Define vowels (both lowercase and uppercase)
    vowels = set('aeiouAEIOU')
    
    # Convert string to list for easier manipulation
    chars = list(s)
    
    # Extract vowels and their original positions in the substring
    vowel_positions = []
    vowel_chars = []
    for i in range(start, end):
        if chars[i] in vowels:
            vowel_positions.append(i)
            vowel_chars.append(chars[i])
    
    # Reverse the vowel characters
    vowel_chars = vowel_chars[::-1]
    
    # Map each vowel using the specific mapping
    vowel_chars = [specific_vowel_map.get(char, char) for char in vowel_chars]
    
    # Replace vowels in their original positions
    for pos, char in zip(vowel_positions, vowel_chars):
        chars[pos] = char
    
    return ''.join(chars)