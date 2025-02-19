def count_non_vowels(input_string):
    """
    Count the number of non-vowel characters in a given string.
    
    Args:
        input_string (str): The input string to count non-vowel characters.
    
    Returns:
        int: Number of non-vowel characters in the string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    vowels = set('aeiou')
    return sum(1 for char in input_string.lower() if char not in vowels and char.isalpha())