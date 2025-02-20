def reverse_string(input_str, method='all'):
    """
    Reverse a string using multiple methods.
    
    :param input_str: String to be reversed
    :param method: Method of reversal ('manual', 'reversed', 'slice', 'split', 'recursive', or 'all')
    :return: Reversed string
    """
    # Manual iteration method
    def manual_reverse(s):
        reversed_str = ''
        for char in s:
            reversed_str = char + reversed_str
        return reversed_str
    
    # Recursively reverse method
    def recursive_reverse(s):
        # Base case
        if len(s) <= 1:
            return s
        # Recursive case
        return recursive_reverse(s[1:]) + s[0]
    
    # Handle different reversal methods
    if method == 'manual':
        return manual_reverse(input_str)
    elif method == 'reversed':
        return ''.join(reversed(input_str))
    elif method == 'slice':
        return input_str[::-1]
    elif method == 'split':
        return ''.join(list(input_str)[::-1])
    elif method == 'recursive':
        return recursive_reverse(input_str)
    elif method == 'all':
        return {
            'manual': manual_reverse(input_str),
            'reversed': ''.join(reversed(input_str)),
            'slice': input_str[::-1],
            'split': ''.join(list(input_str)[::-1]),
            'recursive': recursive_reverse(input_str)
        }
    else:
        raise ValueError(f"Invalid reversal method: {method}")