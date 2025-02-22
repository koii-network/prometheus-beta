def contains_all_vowels(input_string: str) -> bool:
    """
    Check if the given string contains all vowels (a, e, i, o, u).
    
    Args:
        input_string (str): The string to check for vowels.
    
    Returns:
        bool: True if the string contains all vowels, False otherwise.
    """
    # Convert the string to lowercase to handle both uppercase and lowercase
    lowercase_string = input_string.lower()
    
    # Set of vowels to check
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    # Check if all vowels are present in the string
    return all(vowel in lowercase_string for vowel in vowels)