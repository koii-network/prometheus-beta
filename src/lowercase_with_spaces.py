import re

def lowercase_with_spaces(input_string: str) -> str:
    """
    Convert a string to lowercase, replacing non-alphanumeric characters with spaces,
    and adding spaces between camel case words.
    
    Args:
        input_string (str): The input string to be converted.
    
    Returns:
        str: The lowercase string with non-alphanumeric characters replaced by spaces.
    
    Examples:
        >>> lowercase_with_spaces("Hello World!")
        'hello world'
        >>> lowercase_with_spaces("Python_is-AWESOME")
        'python is awesome'
        >>> lowercase_with_spaces("PythonProgramming")
        'python programming'
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # First, add spaces between camel case words
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1 \2', input_string)
    s2 = re.sub('([a-z0-9])([A-Z])', r'\1 \2', s1)
    
    # Convert to lowercase and replace non-alphanumeric characters with spaces
    result = ''.join(char.lower() if char.isalnum() or char.isspace() else ' ' for char in s2)
    
    # Remove extra spaces and strip edges
    return ' '.join(result.split())