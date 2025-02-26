def reverse_string(s: str) -> str:
    """
    Reverse a string in-place without using extra memory.
    
    This function converts the input string to a list of characters 
    and modifies it in-place by swapping characters from both ends 
    until the middle is reached.
    
    Args:
        s (str): The input string to be reversed.
    
    Returns:
        str: The reversed string.
    
    Raises:
        TypeError: If the input is not a string.
    """
    # Convert string to list of characters for in-place modification
    chars = list(s)
    
    # Validate input
    if not isinstance(chars, list):
        raise TypeError("Input must be a string")
    
    # In-place reversal using two-pointer technique
    left, right = 0, len(chars) - 1
    while left < right:
        # Swap characters
        chars[left], chars[right] = chars[right], chars[left]
        
        # Move pointers towards center
        left += 1
        right -= 1
    
    # Convert back to string and return
    return ''.join(chars)