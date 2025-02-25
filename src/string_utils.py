def switch_cases(str1, str2):
    """
    Swap the character cases between two strings.
    
    Args:
        str1 (str): First input string
        str2 (str): Second input string
    
    Returns:
        str: A new string with characters from str1 having the case of str2 
             and characters from str2 having the case of str1
    """
    # Validate input
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Both arguments must be strings")
    
    # Ensure strings are of equal length
    if len(str1) != len(str2):
        raise ValueError("Input strings must be of equal length")
    
    # Swap case logic
    result = ''
    for c1, c2 in zip(str1, str2):
        if c2.isupper():
            result += c1.upper()
        else:
            result += c1.lower()
    
    return result