def to_alternating_dot_case(text):
    """
    Convert a string to alternating dot case.
    
    Args:
        text (str): The input string to convert.
    
    Returns:
        str: The string converted to alternating dot case.
    
    Examples:
        >>> to_alternating_dot_case("hello world")
        'H.e.L.l.O. .W.o.R.l.D'
        >>> to_alternating_dot_case("python programming")
        'P.y.T.h.O.n. .P.r.O.g.R.a.M.m.I.n.G'
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    result = []
    for i, char in enumerate(text):
        if i % 2 == 0:
            result.append(char.upper())
        else:
            result.append(char.lower() + '.')
    
    return ''.join(result).rstrip('.')