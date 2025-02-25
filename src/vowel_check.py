def contains_all_vowels(string: str) -> bool:
    """
    Check if the given string contains all five vowels (a, e, i, o, u).

    Args:
        string (str): The input string to check for vowel containment.

    Returns:
        bool: True if the string contains all vowels, False otherwise.

    Notes:
        - The check is case-insensitive
        - Handles empty strings, returning False
        - Searches for each vowel at least once in the string
    """
    # Convert to lowercase to make the check case-insensitive
    lowered_string = string.lower()
    
    # Set of vowels to check
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    # Check if all vowels are present
    return all(vowel in lowered_string for vowel in vowels)