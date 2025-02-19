def reverse_vowels_in_substring(s, start, end):
    """
    Reverse the vowels in a given substring of a string.
    
    :param s: Input string
    :param start: Start index of the substring (inclusive)
    :param end: End index of the substring (exclusive)
    :return: String with vowels in the specified substring reversed
    """
    # Validate input
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    if not (0 <= start <= end <= len(s)):
        raise ValueError("Invalid substring indices")
    
    # Define vowels (both lowercase and uppercase)
    vowels = set('aeiouAEIOU')
    
    # Convert string to list for easy manipulation
    chars = list(s)
    
    # Extract vowels from the substring
    substring_vowels = [char for char in chars[start:end] if char in vowels]
    
    # If no vowels found, return original string
    if not substring_vowels:
        return s
    
    # Reverse the vowels
    substring_vowels = substring_vowels[::-1]
    
    # Create a new list to build the result
    result_chars = chars.copy()
    
    # Track the index of vowels to replace
    vowel_index = 0
    
    # Replace vowels in the substring
    for i in range(start, end):
        if chars[i] in vowels:
            result_chars[i] = substring_vowels[vowel_index]
            vowel_index += 1
    
    return ''.join(result_chars)