def alternating_kebab_case(input_string):
    """
    Convert a string to alternating kebab case.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The input string converted to alternating kebab case.
    
    Examples:
        >>> alternating_kebab_case("hello world")
        'Hello-world'
        >>> alternating_kebab_case("python is awesome")
        'Python-is-awesome'
        >>> alternating_kebab_case("")
        ''
    """
    if not input_string:
        return ""
    
    # Split the string into words
    words = input_string.split()
    
    # Create alternating kebab case
    result = []
    for i, word in enumerate(words):
        # Capitalize first word, then alternate
        if i == 0:
            result.append(word.capitalize())
        else:
            result.append(word.lower())
    
    # Join with hyphens
    return '-'.join(result)