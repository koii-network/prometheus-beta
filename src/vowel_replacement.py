def replace_vowels(input_string):
    """
    Replace each vowel with the next vowel in the alphabet, preserving case.
    
    Args:
        input_string (str): The input string to modify
    
    Returns:
        str: A new string with vowels replaced
    """
    # Define vowel mappings (lowercase and uppercase)
    vowel_map = {
        'a': 'e', 'e': 'i', 'i': 'o', 'o': 'u', 'u': 'a',
        'A': 'E', 'E': 'I', 'I': 'O', 'O': 'U', 'U': 'A'
    }
    
    # Replace vowels while preserving the original string's structure
    return ''.join(vowel_map.get(char, char) for char in input_string)