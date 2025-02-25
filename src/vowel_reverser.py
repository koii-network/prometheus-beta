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

    # Create a list to track vowel indices and values in the substring
    substring_vowel_indices = []
    substring_vowel_values = []

    # Find vowel positions in the substring
    for i in range(start, end):
        if chars[i] in vowels:
            substring_vowel_indices.append(i)
            substring_vowel_values.append(chars[i])

    # Reverse the vowel values
    substring_vowel_values.reverse()

    # Replace vowels in the substring with reversed vowels
    for i, original_index in enumerate(substring_vowel_indices):
        chars[original_index] = substring_vowel_values[i]

    return ''.join(chars)