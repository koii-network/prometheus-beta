import unicodedata

def count_vowels_and_consonants(input_string):
    """
    Count the number of vowels and consonants in a given string.
    
    Args:
        input_string (str): The input string to analyze.
    
    Returns:
        dict: A dictionary with 'vowels' and 'consonants' count.
    
    Raises:
        TypeError: If input is not a string.
    """
    # Validate input
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Normalize unicode characters and convert to lowercase
    input_string = unicodedata.normalize('NFKD', input_string.lower())
    
    # Define vowels (including some unicode variations)
    vowels = set('aeiouÃ¡Ã©Ã­Ã³ÃºÃ¤Ã«Ã¯Ã¶Ã¼Ã¢ÃªÃ®Ã´Ã»')
    
    # Initialize counters
    vowel_count = 0
    consonant_count = 0
    
    # Count vowels and consonants
    for char in input_string:
        # Remove accents for character check
        stripped_char = ''.join(c for c in unicodedata.normalize('NFKD', char) 
                                if unicodedata.category(c) != 'Mn')
        
        # Check if character is alphabetic
        if stripped_char.isalpha():
            if stripped_char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    
    return {
        'vowels': vowel_count,
        'consonants': consonant_count
    }