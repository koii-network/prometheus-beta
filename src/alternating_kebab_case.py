def to_alternating_kebab_case(input_string):
    """
    Convert a string to alternating kebab case.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The string converted to alternating kebab case.
    
    Raises:
        TypeError: If input is not a string.
    """
    # Validate input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Remove any existing non-alphanumeric characters and split
    words = ''.join(char if char.isalnum() or char.isspace() else ' ' for char in input_string).split()
    
    # Convert to alternating kebab case
    alternating_case = []
    for i, word in enumerate(words):
        # Alternate between lowercase and uppercase
        if i % 2 == 0:
            alternating_case.append(word.lower())
        else:
            alternating_case.append(word.upper())
    
    # Join with kebab case (hyphen)
    return '-'.join(alternating_case)