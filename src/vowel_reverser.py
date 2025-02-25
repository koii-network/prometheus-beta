def reverse_vowels_in_substring(s: str, start: int, end: int) -> str:
    """
    Reverse the vowels within a specified substring of a given string.

    Args:
        s (str): The input string.
        start (int): The starting index of the substring (inclusive).
        end (int): The ending index of the substring (exclusive).

    Returns:
        str: A new string with vowels in the specified substring reversed.

    Raises:
        ValueError: If start or end indices are out of bounds.
        ValueError: If start index is greater than end index.
    """
    # Validate input indices
    if start < 0 or end > len(s):
        raise ValueError("Start or end indices are out of bounds.")
    if start > end:
        raise ValueError("Start index must be less than or equal to end index.")

    # Define vowels (both lowercase and uppercase)
    vowels = set('aeiouAEIOU')

    # Convert string to list for easier manipulation
    chars = list(s)

    # Extract vowels from the substring
    substring_vowels = [char for char in chars[start:end] if char in vowels]
    
    # Reverse the vowels 
    substring_vowels.reverse()

    # Create a new list to build the result
    result_chars = chars.copy()

    # Replace vowels in the substring with reversed vowels
    vowel_index = 0
    for i in range(start, end):
        if chars[i] in vowels:
            result_chars[i] = substring_vowels[vowel_index]
            vowel_index += 1

    return ''.join(result_chars)