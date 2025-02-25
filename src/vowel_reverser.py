def reverse_vowels_in_substring(s: str, start: int, end: int) -> str:
    """
    Reverse the vowels within a specified substring of a given string.

    Args:
        s (str): The input string
        start (int): The starting index of the substring (inclusive)
        end (int): The ending index of the substring (exclusive)

    Returns:
        str: A new string with vowels in the specified substring reversed

    Raises:
        ValueError: If start or end indices are out of bounds
        TypeError: If inputs are not of correct type
    """
    # Validate input types
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("Start and end indices must be integers")

    # Validate index bounds
    if start < 0 or end > len(s) or start >= end:
        raise ValueError("Invalid substring indices")

    # Define vowels (both lowercase and uppercase)
    vowels = set('aeiouAEIOU')

    # Convert string to list for easier manipulation
    chars = list(s)

    # Extract vowels from the substring
    substring_vowels = [char for char in chars[start:end] if char in vowels]
    
    # Reverse the extracted vowels
    substring_vowels.reverse()

    # Create a new list to build the result
    result = chars.copy()

    # Replace vowels in the substring with reversed vowels
    vowel_index = 0
    for i in range(start, end):
        if chars[i] in vowels:
            result[i] = substring_vowels[vowel_index]
            vowel_index += 1

    # Convert back to string
    return ''.join(result)