def switch_cases(str1: str, str2: str) -> str:
    """
    Take two strings and return a new string with swapped character cases.
    
    Args:
        str1 (str): First input string
        str2 (str): Second input string
    
    Returns:
        str: A new string where characters from str1 have their case swapped 
             and characters from str2 remain in their original case
    """
    # Swap the case of characters in str1
    swapped_str1 = ''.join(
        char.lower() if char.isupper() else char.upper() 
        for char in str1
    )
    
    return swapped_str1