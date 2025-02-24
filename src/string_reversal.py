def reverse_string_in_place(s: str) -> str:
    """
    Reverses a string in-place without using extra memory.
    
    Args:
        s (str): The input string to be reversed.
    
    Returns:
        str: The reversed string.
    
    Raises:
        TypeError: If the input is not a string.
    """
    # Convert string to list of characters (strings are immutable in Python)
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Convert string to list for in-place reversal
    chars = list(s)
    
    # Two-pointer approach for in-place reversal
    left, right = 0, len(chars) - 1
    while left < right:
        # Swap characters
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    
    # Convert back to string
    return ''.join(chars)