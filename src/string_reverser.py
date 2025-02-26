def reverse_string_in_place(s: str) -> str:
    """
    Reverse the characters in a string in-place without using extra memory.
    
    Args:
        s (str): The input string to be reversed.
    
    Returns:
        str: The reversed string.
    
    Raises:
        TypeError: If input is not a string.
    """
    # Convert string to list of characters as strings are immutable in Python
    chars = list(s)
    
    # Validate input
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Two-pointer approach to reverse in-place
    left, right = 0, len(chars) - 1
    while left < right:
        # Swap characters
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    
    # Convert back to string
    return ''.join(chars)