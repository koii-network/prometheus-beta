def switch_cases(str1, str2):
    """
    Takes two strings and returns a new string with swapped character cases.
    
    Args:
        str1 (str): First input string
        str2 (str): Second input string
    
    Returns:
        str: A new string where the case of each character is swapped
    """
    # Combine the two input strings
    combined = str1 + str2
    
    # Switch cases for each character
    switched = ''.join(
        char.lower() if char.isupper() else char.upper() 
        for char in combined
    )
    
    return switched