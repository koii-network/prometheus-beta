def count_vowels_and_consonants(text: str) -> dict:
    """
    Count the number of vowels and consonants in a given string.
    
    Args:
        text (str): Input string to analyze
    
    Returns:
        dict: A dictionary with 'vowels' and 'consonants' count
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # Convert to lowercase to simplify counting
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