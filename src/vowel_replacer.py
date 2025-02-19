def replace_vowels(input_string):
    """
    Replace each vowel with the next vowel in the alphabet, preserving case.
    
    Args:
        input_string (str): The input string to modify.
    
    Returns:
        str: A new string with vowels replaced.
    """
    vowels = 'aeiou'
    vowels_upper = 'AEIOU'
    
    def replace_vowel(char):
        # Handle lowercase vowels
        if char.lower() in vowels:
            current_index = vowels.index(char.lower())
            next_index = (current_index + 1) % len(vowels)
            next_vowel = vowels[next_index]
            return next_vowel if char.islower() else next_vowel.upper()
        return char
    
    return ''.join(replace_vowel(char) for char in input_string)