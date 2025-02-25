def convert_to_sentence_case(text: str) -> str:
    """
    Convert a string to sentence case.
    
    Sentence case capitalizes the first character of the first non-whitespace 
    character and ensures the rest are lowercase while preserving original whitespace.
    
    Args:
        text (str): The input string to convert to sentence case.
    
    Returns:
        str: The input string converted to sentence case.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> convert_to_sentence_case("HELLO WORLD")
        'Hello world'
        >>> convert_to_sentence_case("hello WORLD")
        'Hello world'
        >>> convert_to_sentence_case("")
        ''
        >>> convert_to_sentence_case(" HELLO ")
        ' Hello '
    """
    # Check if input is a string
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if not text:
        return text
    
    # Find the first non-whitespace character
    first_non_whitespace_index = 0
    for i, char in enumerate(text):
        if not char.isspace():
            first_non_whitespace_index = i
            break
    
    # Create the sentence case string
    modified_text = list(text)
    modified_text[first_non_whitespace_index] = text[first_non_whitespace_index].upper()
    
    for i in range(first_non_whitespace_index + 1, len(text)):
        modified_text[i] = text[i].lower()
    
    return ''.join(modified_text)