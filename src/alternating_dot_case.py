def convert_to_alternating_dot_case(input_string):
    """
    Convert a string to alternating dot case.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The string converted to alternating dot case.
    
    Raises:
        TypeError: If input is not a string.
    
    Examples:
        >>> convert_to_alternating_dot_case("hello world")
        'h.e.l.l.o. .w.o.r.l.d'
        >>> convert_to_alternating_dot_case("Python")
        'P.y.t.h.o.n'
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    return '.'.join(char for char in input_string)