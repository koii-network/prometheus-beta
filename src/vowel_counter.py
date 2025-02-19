def count_vowels(text: str) -> int:
    """
    Count the number of vowels in a given string case-insensitively.
    
    Args:
        text (str): The input string to count vowels in.
    
    Returns:
        int: The total number of vowels (a, e, i, o, u) in the string.
    """
    # Convert the text to lowercase to make counting case-insensitive
    text = text.lower()
    
    # Define the set of vowels
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    # Count the number of vowels
    vowel_count = sum(1 for char in text if char in vowels)
    
    return vowel_count