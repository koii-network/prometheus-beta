"""
Module for reversing strings using multiple methods.

This module provides a comprehensive string reversal function that supports
multiple reversal techniques, demonstrating different Python string manipulation approaches.
"""

def reverse_string(input_str, method='all'):
    """
    Reverse a string using multiple methods.

    Args:
        input_str (str): The string to be reversed
        method (str, optional): The specific reversal method to use. 
            Defaults to 'all', which returns a dictionary of all methods.
            Options: 'manual', 'reversed', 'slicing', 'splitjoin', 'recursive', 'all'

    Returns:
        str or dict: Reversed string or dictionary of reversed strings

    Raises:
        TypeError: If input is not a string
        ValueError: If an invalid method is specified
    """
    # Type checking
    if not isinstance(input_str, str):
        raise TypeError("Input must be a string")

    # Manual iteration method
    def manual_reverse(s):
        reversed_str = ''
        for char in s:
            reversed_str = char + reversed_str
        return reversed_str

    # Reversed() method
    def reversed_method(s):
        return ''.join(reversed(s))

    # Slicing method
    def slicing_method(s):
        return s[::-1]

    # Split/Reverse/Join method
    def split_reverse_join(s):
        return ''.join(list(s)[::-1])

    # Recursive method
    def recursive_method(s):
        # Base case
        if len(s) <= 1:
            return s
        # Recursive case
        return recursive_method(s[1:]) + s[0]

    # Method selection and execution
    methods = {
        'manual': manual_reverse,
        'reversed': reversed_method,
        'slicing': slicing_method,
        'splitjoin': split_reverse_join,
        'recursive': recursive_method
    }

    # Validate method
    if method != 'all' and method not in methods:
        raise ValueError(f"Invalid method. Choose from {list(methods.keys())} or 'all'")

    # Return results
    if method == 'all':
        return {method: func(input_str) for method, func in methods.items()}
    else:
        return methods[method](input_str)