def convert_to_title_case(input_string: str) -> str:
    """
    Convert a given string to title case.
    
    Title case converts the first letter of each word to uppercase,
    while making the rest of the letters lowercase. Preserves hyphenated
    words' individual capitalization.
    
    Args:
        input_string (str): The input string to be converted to title case.
    
    Returns:
        str: The input string converted to title case.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> convert_to_title_case("hello world")
        'Hello World'
        >>> convert_to_title_case("PYTHON PROGRAMMING")
        'Python Programming'
        >>> convert_to_title_case("python-programming language")
        'Python-Programming Language'
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if not input_string:
        return ""
    
    # Split the string by spaces
    words = input_string.split()
    
    # Capitalize each word, preserving hyphenated parts
    title_case_words = []
    for word in words:
        # If word contains a hyphen, capitalize each part
        if '-' in word:
            hyphen_parts = word.split('-')
            hyphen_title = '-'.join(part.capitalize() for part in hyphen_parts)
            title_case_words.append(hyphen_title)
        else:
            # Regular word capitalization
            title_case_words.append(word.capitalize())
    
    return ' '.join(title_case_words)