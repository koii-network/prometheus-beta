def to_alternating_camel_case(s: str) -> str:
    """
    Convert a string to alternating camel case.
    
    In alternating camel case, every other word starts with a capital letter,
    with the first word always starting in lowercase.
    
    Args:
        s (str): The input string to convert
    
    Returns:
        str: The string converted to alternating camel case
    
    Raises:
        TypeError: If input is not a string
    
    Examples:
        >>> to_alternating_camel_case("hello world python")
        'helloWorldPython'
        >>> to_alternating_camel_case("this is a test")
        'thisIsATest'
    """
    # Check input type
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if not s:
        return ""
    
    # Split the string into words and handle special cases
    words = s.split()
    
    # Convert to alternating camel case
    result = words[0].lower()
    for i, word in enumerate(words[1:], 1):
        # Fully capitalize words at odd indices (starting from 1)
        result += word.upper() if i % 2 == 1 else word.lower()
    
    return result