def contains_all_vowels(text: str) -> bool:
    """
    Check if the given string contains all vowels (a, e, i, o, u).
    
    Args:
        text (str): The input string to check for vowels.
    
    Returns:
        bool: True if the string contains all vowels, False otherwise.
    """
    # Convert to lowercase to make the check case-insensitive
    text_lower = text.lower()
    
    # Set of vowels to check
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    # Check if all vowels are present in the string
    return all(vowel in text_lower for vowel in vowels)