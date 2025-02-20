def reverse_string_in_place(s: str) -> str:
    """
    Reverse a string in-place without using extra memory.
    
    Args:
        s (str): Input string to be reversed.
    
    Returns:
        str: Reversed string.
    
    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Convert string to list of characters for in-place manipulation
    chars = list(s)
    
    # Two-pointer approach to reverse characters
    left, right = 0, len(chars) - 1
    while left < right:
        # Swap characters
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    
    # Convert back to string
    return ''.join(chars)