def count_vowels_consonants(input_string):
    """
    Count the number of vowels and consonants in a given string.
    
    Args:
        input_string (str): The input string to analyze.
    
    Returns:
        dict: A dictionary with 'vowels' and 'consonants' count.
    
    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Convert to lowercase to simplify counting
    input_string = input_string.lower()
    
    # Define vowels
    vowels = 'aeiou'
    
    # Initialize counters
    vowel_count = 0
    consonant_count = 0
    
    # Count vowels and consonants
    for char in input_string:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    
    return {
        'vowels': vowel_count, 
        'consonants': consonant_count
    }