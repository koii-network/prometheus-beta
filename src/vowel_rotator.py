def rotate_vowels(input_string):
    """
    Replace each vowel in the input string with the next vowel in the alphabet, 
    preserving the original case.
    
    Args:
        input_string (str): The input string to rotate vowels in.
    
    Returns:
        str: A new string with vowels rotated.
    
    Examples:
        >>> rotate_vowels("hello")
        'holli'
        >>> rotate_vowels("AEIOU")
        'EIOUA'
        >>> rotate_vowels("Python")
        'Pythen'
    """
    # Define vowel rotation mappings (both lowercase and uppercase)
    vowel_map = {
        'a': 'e', 'e': 'i', 'i': 'o', 'o': 'u', 'u': 'a',
        'A': 'E', 'E': 'I', 'I': 'O', 'O': 'U', 'U': 'A'
    }
    
    # Rotate vowels while preserving non-vowel characters
    return ''.join(vowel_map.get(char, char) for char in input_string)