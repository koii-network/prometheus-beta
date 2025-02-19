def count_vowels_consonants(text):
    """
    Count the number of vowels and consonants in a given string of English text.
    
    Args:
        text (str): Input string to analyze
    
    Returns:
        dict: A dictionary containing the count of vowels and consonants
    """
    # Normalize the text to lowercase to simplify counting
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
    
    return {
        'vowels': vowel_count,
        'consonants': consonant_count
    }