def to_alternating_pascal_case(text: str) -> str:
    """
    Convert a string to alternating Pascal case.
    
    Args:
        text (str): The input string to convert.
    
    Returns:
        str: The string converted to alternating Pascal case.
    
    Examples:
        >>> to_alternating_pascal_case("hello world")
        'HeLlO WoRlD'
        >>> to_alternating_pascal_case("python is awesome")
        'PyThOn Is AwEsOmE'
    """
    if not text:
        return ""
    
    words = text.split()
    alternating_words = []
    
    for word in words:
        alternating_chars = []
        for i, char in enumerate(word):
            if i % 2 == 0:
                alternating_chars.append(char.upper())
            else:
                alternating_chars.append(char.lower())
        
        alternating_word = ''.join(alternating_chars)
        alternating_words.append(alternating_word)
    
    return ' '.join(alternating_words)