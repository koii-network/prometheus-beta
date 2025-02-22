def count_vowels_and_consonants(text):
    """
    Count the number of vowels and consonants in a given string of English text.
    
    Args:
        text (str): Input text to analyze
    
    Returns:
        tuple: A tuple containing (vowel_count, consonant_count)
    """
    # Convert text to lowercase for consistent counting
    text = text.lower()
    
    # Define vowels
    vowels = set('aeiou')
    
    # Initialize counters
    vowel_count = 0
    consonant_count = 0
    
    # Count vowels and consonants
    for char in text:
        # Check if character is an alphabetic letter
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    
    return (vowel_count, consonant_count)