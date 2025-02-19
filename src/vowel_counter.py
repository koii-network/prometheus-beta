def count_vowels(text: str) -> int:
    """
    Count the number of vowels in a given text, case-insensitively.
    
    Args:
        text (str): The input text to count vowels in.
    
    Returns:
        int: The total number of vowels in the text.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # Convert to lowercase to make counting case-insensitive
    text = text.lower()
    
    # Define vowels
    vowels = set('aeiou')
    
    # Count vowels using a generator expression
    return sum(1 for char in text if char in vowels)