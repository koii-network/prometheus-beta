def count_vowels_consonants(text):
    """
    Count the number of vowels and consonants in a given string of English text.
    
    Args:
        text (str): Input text to analyze
    
    Returns:
        dict: A dictionary with 'vowels' and 'consonants' count
    
    Raises:
        TypeError: If input is not a string
        ValueError: If input is an empty string
    """
    # Input validation
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    if not text.strip():
        raise ValueError("Input string cannot be empty")
    
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
    
    return {
        'vowels': vowel_count,
        'consonants': consonant_count
    }