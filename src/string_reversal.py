def reverse_string_manual(s: str) -> str:
    """
    Reverse a string using manual iteration.
    
    Args:
        s (str): Input string to reverse
    
    Returns:
        str: Reversed string
    """
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

def reverse_string_reversed(s: str) -> str:
    """
    Reverse a string using built-in reversed() function.
    
    Args:
        s (str): Input string to reverse
    
    Returns:
        str: Reversed string
    """
    return ''.join(reversed(s))

def reverse_string_slicing(s: str) -> str:
    """
    Reverse a string using slicing.
    
    Args:
        s (str): Input string to reverse
    
    Returns:
        str: Reversed string
    """
    return s[::-1]

def reverse_string_split_reverse_join(s: str) -> str:
    """
    Reverse a string using split(), reverse(), and join() methods.
    
    Args:
        s (str): Input string to reverse
    
    Returns:
        str: Reversed string
    """
    return ''.join(list(s)[::-1])

def reverse_string_recursive(s: str) -> str:
    """
    Reverse a string recursively.
    
    Args:
        s (str): Input string to reverse
    
    Returns:
        str: Reversed string
    """
    # Base case: empty string or single character
    if len(s) <= 1:
        return s
    
    # Recursive case: first char moved to end, rest of string reversed
    return reverse_string_recursive(s[1:]) + s[0]