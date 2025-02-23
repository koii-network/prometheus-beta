import unicodedata

def count_vowels(text: str) -> int:
    """
    Count the number of vowels in the given text (case-insensitive).

    Args:
        text (str): The input text to count vowels in.

    Returns:
        int: The total number of vowels (a, e, i, o, u) in the text.

    Examples:
        >>> count_vowels("Hello")
        2
        >>> count_vowels("WORLD")
        1
        >>> count_vowels("aEiOu")
        5
        >>> count_vowels("áéíóú")
        5
    """
    # Define vowels (lowercase for case-insensitive comparison)
    vowels = set('aeiouáéíóú')
    
    # Normalize unicode characters and convert to lowercase
    normalized_text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8').lower()
    
    # Count vowels
    return sum(1 for char in normalized_text if char in vowels)