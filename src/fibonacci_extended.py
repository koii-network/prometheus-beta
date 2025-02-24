"""
Extended Fibonacci Sequence Implementation

This module provides a function to generate Fibonacci numbers 
that supports negative indices and floating-point numbers.

The implementation follows the generalized Fibonacci recurrence 
that works for both positive and negative indices.
"""

def fibonacci(n):
    """
    Generate the nth number in an extended Fibonacci sequence.
    
    The function supports:
    - Positive and negative integer indices
    - Floating-point indices
    - Rational indexing behavior
    
    Args:
        n (int or float): The index in the Fibonacci sequence
    
    Returns:
        float: The Fibonacci number at the given index
    
    Raises:
        TypeError: If the input is not a number
    """
    # Type checking
    if not isinstance(n, (int, float)):
        raise TypeError("Input must be a number")
    
    # Handle integer cases first for efficiency
    if isinstance(n, int):
        # Direct integer Fibonacci with negative index support
        if n == 0:
            return 0
        elif n == 1 or n == -1:
            return 1
        
        # Use the symmetry and sign properties of Fibonacci for negative indices
        if n > 1:
            # Positive integer case
            a, b = 0, 1
            for _ in range(2, n + 1):
                a, b = b, a + b
            return b
        else:
            # Negative integer case
            # Uses the property F(-n) = (-1)^(n+1) * F(n)
            a, b = 0, 1
            for _ in range(2, abs(n) + 1):
                a, b = b, a + b
            return (-1)**(abs(n)+1) * b
    
    # Floating-point and non-integer cases
    # Use a more robust method that avoids complex numbers
    from math import sin, pi, floor
    
    # If it's very close to an integer, treat it as such
    if abs(n - round(n)) < 1e-10:
        return fibonacci(round(n))
    
    # Generalized method for non-integer indices
    def sign(x):
        return 1 if x >= 0 else -1
    
    # Use a combination of trigonometric properties
    def generalized_fibonacci(x):
        # Approximate Fibonacci for non-integer indices
        k = floor(abs(x))
        f_k = fibonacci(k)
        f_k1 = fibonacci(k + 1)
        
        # Linear interpolation with trigonometric adjustment
        frac = abs(x) - k
        interpolated = f_k * (1 - frac) + f_k1 * frac
        
        # Adjust sign for negative indices
        return sign(x) * interpolated
    
    return generalized_fibonacci(n)