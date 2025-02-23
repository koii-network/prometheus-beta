import re

def to_alternating_kebab_case(text: str) -> str:
    """
    Convert a string to alternating kebab case.
    
    Alternating kebab case converts the string into a kebab-case format 
    where each word alternates between lowercase and uppercase.
    
    Args:
        text (str): The input string to convert.
    
    Returns:
        str: The string converted to alternating kebab case.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> to_alternating_kebab_case("hello world")
        'hello-World'
        >>> to_alternating_kebab_case("PYTHON PROGRAMMING")
        'python-Programming'
        >>> to_alternating_kebab_case("snake_case example")
        'snake-Case-Example'
    """
    # Check input type
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # Remove special characters, replace underscores and existing dashes with space
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text).replace('_', ' ').replace('-', ' ')
    
    # Split into words, removing empty strings
    words = [word for word in cleaned_text.split() if word]
    
    # Convert words with alternating case
    alternating_words = []
    for i, word in enumerate(words):
        # First word is lowercase, then alternate
        if i % 2 == 0:
            alternating_words.append(word.lower())
        else:
            alternating_words.append(word.capitalize())
    
    # Join with dash, handle empty list case
    return '-'.join(alternating_words) if alternating_words else ''