def reverse_string(input_string, method='manual'):
    """
    Reverse a string using multiple methods.
    
    :param input_string: The string to be reversed
    :param method: Method of reversal ('manual', 'reversed', 'slicing', 'split', 'recursive')
    :return: Reversed string
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    if method == 'manual':
        # Manual iteration reversal
        reversed_str = ''
        for char in input_string:
            reversed_str = char + reversed_str
        return reversed_str
    
    elif method == 'reversed':
        # Using built-in reversed() function
        return ''.join(reversed(input_string))
    
    elif method == 'slicing':
        # Using string slicing
        return input_string[::-1]
    
    elif method == 'split':
        # Using split(), reverse(), and join()
        return ''.join(list(input_string)[::-1])
    
    elif method == 'recursive':
        # Recursive string reversal
        if len(input_string) <= 1:
            return input_string
        return reverse_string(input_string[1:]) + input_string[0]
    
    else:
        raise ValueError("Invalid reversal method. Choose 'manual', 'reversed', 'slicing', 'split', or 'recursive'.")