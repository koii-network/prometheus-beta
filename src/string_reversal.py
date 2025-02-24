def reverse_string_in_place(s: str) -> str:
    """
    Reverse the characters in a string in-place without using extra memory.
    
    This function converts the input string to a list of characters to allow 
    in-place modification, as strings are immutable in Python.
    
    Args:
        s (str): The input string to be reversed
    
    Returns:
        str: The reversed string
    
    Raises:
        TypeError: If input is not a string
    
    Time Complexity: O(n)
    Space Complexity: O(1) after converting to list
    
    Examples:
        >>> reverse_string_in_place("hello")
        'olleh'
        >>> reverse_string_in_place("")
        ''
        >>> reverse_string_in_place("a")
        'a'
    """
    # Check for invalid input
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Convert string to list of characters for in-place modification
    chars = list(s)
    
    # Two-pointer approach to swap characters
    left, right = 0, len(chars) - 1
    while left < right:
        # Swap characters
        chars[left], chars[right] = chars[right], chars[left]
        
        # Move pointers
        left += 1
        right -= 1
    
    # Convert back to string and return
    return ''.join(chars)