def count_vowels(text: str) -> int:
    """
    Count the number of vowels in the given text case-insensitively.
    
    Args:
        text (str): The input text to count vowels in.
    
    Returns:
        int: The total number of vowels (a, e, i, o, u) in the text.
    """
    # Define vowels (both lowercase and uppercase)
    vowels = set('aeiouAEIOU')
    
    # Count vowels in the text
    return sum(1 for char in text if char in vowels)