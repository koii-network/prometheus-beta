def reverse_string(text, method='all'):
    """
    Reverse a string using multiple methods.
    
    Args:
        text (str): The string to be reversed
        method (str, optional): The reversal method to use. 
                                Defaults to 'all', which returns a dict of all methods.
    
    Returns:
        str or dict: Reversed string or dictionary of reversed strings
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    methods = {
        # Manual iteration method
        'manual': manual_reverse(text),
        
        # Using built-in reversed() function
        'reversed': reversed_method(text),
        
        # Using string slicing
        'slicing': slicing_method(text),
        
        # Using split/reverse/join method
        'split_reverse': split_reverse_method(text),
        
        # Recursive method
        'recursive': recursive_reverse(text)
    }
    
    if method == 'all':
        return methods
    
    if method not in methods:
        raise ValueError(f"Invalid method. Choose from {list(methods.keys())}")
    
    return methods[method]

def manual_reverse(text):
    """Reverse string using manual iteration."""
    reversed_str = ''
    for char in text:
        reversed_str = char + reversed_str
    return reversed_str

def reversed_method(text):
    """Reverse string using built-in reversed() function."""
    return ''.join(reversed(text))

def slicing_method(text):
    """Reverse string using string slicing."""
    return text[::-1]

def split_reverse_method(text):
    """Reverse string using split/reverse/join method."""
    return ''.join(list(text)[::-1])

def recursive_reverse(text):
    """Reverse string recursively."""
    if len(text) <= 1:
        return text
    return recursive_reverse(text[1:]) + text[0]