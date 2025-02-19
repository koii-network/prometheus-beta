def contains_all_vowels(string: str) -> bool:
    """
    Check if the given string contains all vowels (a, e, i, o, u).
    
    Args:
        string (str): The input string to check for vowels.
    
    Returns:
        bool: True if the string contains all vowels, False otherwise.
    """
    # Convert the string to lowercase to make the check case-insensitive
    string = string.lower()
    
    # Set of vowels to check
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    # Check if all vowels are in the string
    return all(vowel in string for vowel in vowels)