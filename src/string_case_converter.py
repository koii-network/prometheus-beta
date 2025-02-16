def convert_to_alternate_path_case(input_string):
    """
    Convert a string to alternating path case.

    Args:
        input_string (str): The input string to convert.

    Returns:
        str: The string converted to alternating path case.

    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")

    # Handle empty string
    if not input_string:
        return ""

    # Split the string into words
    words = input_string.split()
    
    # Convert words to alternating case
    alternate_words = []
    for i, word in enumerate(words):
        if i % 2 == 0:
            # Even indices (0, 2, 4...) use lowercase
            alternate_words.append(word.lower())
        else:
            # Odd indices (1, 3, 5...) use uppercase
            alternate_words.append(word.upper())
    
    # Join the words with hyphens
    return "-".join(alternate_words)