def contains_all_vowels(input_string: str) -> bool:
    """
    Check if the given string contains all vowels (a, e, i, o, u).
    
    Args:
        input_string (str): The string to check for vowel presence.
    
    Returns:
        bool: True if the string contains all vowels, False otherwise.
    """
    # Convert the string to lowercase to handle both uppercase and lowercase vowels
    input_string = input_string.lower()
    
    # Set of vowels to check
    vowels = set('aeiou')
    
    # Check if all vowels are present in the input string
    return vowels.issubset(set(input_string))