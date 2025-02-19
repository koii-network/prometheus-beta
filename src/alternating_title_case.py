def convert_to_alternating_title_case(input_string):
    """
    Convert a string to alternating title case.
    
    Args:
        input_string (str): The input string to be converted.
    
    Returns:
        str: A string with words alternating between title case and lower case.
    
    Raises:
        TypeError: If input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Split the string into words
    words = input_string.split()
    
    # Convert words to alternating case
    alternating_words = [
        word.title() if index % 2 == 0 else word.lower() 
        for index, word in enumerate(words)
    ]
    
    # Join the words back together
    return ' '.join(alternating_words)