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
    
    # Replace underscores and existing dashes with space
    processed_text = text.replace('_', ' ').replace('-', ' ')
    
    # Split words and remove/filter special characters
    words = []
    for word in processed_text.split():
        # Remove special characters, but preserve word structure
        clean_word = re.sub(r'[^a-zA-Z]', '', word)
        if clean_word:
            words.append(clean_word)
    
    # Convert words with alternating case, ensuring each word is properly cased
    alternating_words = []
    for i, word in enumerate(words):
        # First word is lowercase, then alternate, and fully capitalize even words
        if i % 2 == 0:
            alternating_words.append(word.lower())
        else:
            alternating_words.append(word.capitalize())
    
    # Join with dash, handle empty list case
    return '-'.join(alternating_words) if alternating_words else ''