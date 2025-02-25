def count_non_vowel_characters(input_string: str) -> int:
    """
    Count the number of non-vowel characters in the given string.
    
    Args:
        input_string (str): The input string to analyze.
    
    Returns:
        int: The number of non-vowel characters in the string.
    
    Notes:
        - Vowels are considered case-insensitive (a, e, i, o, u)
        - Empty string returns 0
        - Non-alphabetic characters are counted as non-vowels
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Define vowels (lowercase)
    vowels = set('aeiou')
    
    # Count non-vowel characters
    return sum(1 for char in input_string.lower() if char not in vowels)