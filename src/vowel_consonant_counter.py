def count_vowels_and_consonants(text):
    """
    Count the number of vowels and consonants in a given string.
    
    Args:
        text (str): The input string to analyze.
    
    Returns:
        tuple: A tuple containing (vowel_count, consonant_count)
    
    Raises:
        TypeError: If input is not a string
    """
    # Check input type
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
        # Only count alphabetic characters
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    
    return (vowel_count, consonant_count)