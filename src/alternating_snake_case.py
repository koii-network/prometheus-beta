def convert_to_alternating_snake_case(input_string: str) -> str:
    """
    Convert a given string to alternating snake case.
    
    Alternating snake case means the words are separated by underscores,
    and the words alternate between lowercase and uppercase.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The string converted to alternating snake case.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> convert_to_alternating_snake_case("hello world")
        'hello_World'
        >>> convert_to_alternating_snake_case("python is awesome")
        'python_Is_awesome'
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If input is empty, return empty string
    if not input_string:
        return ""
    
    # Split the input into words
    words = input_string.split()
    
    # Convert words alternately
    converted_words = []
    for i, word in enumerate(words):
        if i % 2 == 0:
            # Even index words (0, 2, 4...) remain lowercase
            converted_words.append(word.lower())
        else:
            # Odd index words (1, 3, 5...) are capitalized
            converted_words.append(word.capitalize())
    
    # Join with underscores
    return '_'.join(converted_words)