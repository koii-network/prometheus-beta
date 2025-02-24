def count_vowels_consonants(text):
    """
    Count the number of vowels and consonants in a given string.
    
    Args:
        text (str): The input string to analyze.
    
    Returns:
        dict: A dictionary with 'vowels' and 'consonants' counts.
    
    Raises:
        TypeError: If input is not a string.
    """
    # Validate input type
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # Convert to lowercase for consistent counting
    text = text.lower()
    
    # Define vowels
    vowels = set('aeiou')
    
    # Initialize counters
    vowel_count = 0
    consonant_count = 0
    
    # Count vowels and consonants
    for char in text:
        # Check if the character is a letter (handling unicode)
        if char.isalpha():
            # Normalize accented characters to their base form
            base_char = char.translate(str.maketrans('áéíóúäëïöü', 'aeiouaeioue'))
            
            if base_char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    
    return {
        'vowels': vowel_count,
        'consonants': consonant_count
    }