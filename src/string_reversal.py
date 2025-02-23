def reverse_string_in_place(s: str) -> str:
    """
    Reverse a string in-place without using extra memory.
    
    Note: In Python, strings are immutable, so we'll convert to a list first 
    to simulate in-place reversal while minimizing memory usage.
    
    Args:
        s (str): Input string to be reversed
    
    Returns:
        str: Reversed string
    
    Raises:
        TypeError: If input is not a string
    """
    # Check input type
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Convert to list of characters for in-place modification
    chars = list(s)
    
    # Two-pointer approach to reverse in-place
    left, right = 0, len(chars) - 1
    while left < right:
        # Swap characters
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    
    # Convert back to string
    return ''.join(chars)