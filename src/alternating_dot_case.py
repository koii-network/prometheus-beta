def to_alternating_dot_case(text: str) -> str:
    """
    Convert a string to alternating dot case.
    
    Args:
        text (str): The input string to convert.
    
    Returns:
        str: The string converted to alternating dot case.
    
    Examples:
        >>> to_alternating_dot_case("hello world")
        'h.e.l.l.o. .w.o.r.l.d'
        >>> to_alternating_dot_case("python")
        'p.y.t.h.o.n'
        >>> to_alternating_dot_case("")
        ''
    """
    if not text:
        return ""
    
    return '.'.join(char for char in text)