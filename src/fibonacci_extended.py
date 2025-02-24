"""
Extended Fibonacci Sequence Implementation

This module provides a function to generate Fibonacci numbers 
that supports negative indices and floating-point numbers.

The implementation follows the generalized Fibonacci recurrence 
that works for both positive and negative indices.
"""

import math

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
    # Binet's formula with careful handling
    phi = (1 + math.sqrt(5)) / 2
    psi = (1 - math.sqrt(5)) / 2
    
    # Generalized Fibonacci formula with sign correction
    def safe_power(base, exp):
        """Safely handle power operations to avoid complex numbers."""
        # Handle sign separately
        sign = 1 if exp >= 0 else -1
        abs_exp = abs(exp)
        
        # Compute the base raised to the absolute value of the exponent
        try:
            result = abs(base) ** abs_exp
        except Exception:
            # Fallback to math.pow if ** fails
            result = math.pow(abs(base), abs_exp)
        
        # Apply sign correction if exponent is negative
        return sign * result
    
    # Careful computation avoiding complex numbers
    # Breaking down the Binet formula to handle edge cases
    def generalized_fib(x):
        # Adjust for potential floating-point precision issues
        term1 = safe_power(phi, x)
        term2 = safe_power(psi, x)
        return (term1 - term2) / math.sqrt(5)
    
    return generalized_fib(n)