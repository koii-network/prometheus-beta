def count_vowels_and_consonants(text: str) -> dict:
    """
    Count the number of vowels and consonants in a given string of English text.
    
    Args:
        text (str): The input text to analyze
    
    Returns:
        dict: A dictionary with 'vowels' and 'consonants' count
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
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    
    return {
        'vowels': vowel_count,
        'consonants': consonant_count
    }