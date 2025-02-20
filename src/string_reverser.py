def reverse_string_in_place(s: list) -> None:
    """
    Reverse a string in-place by modifying the input list of characters.
    
    Args:
        s (list): A mutable list of characters to be reversed.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Example:
        >>> chars = list('hello')
        >>> reverse_string_in_place(chars)
        >>> ''.join(chars)
        'olleh'
    """
    # Check for empty or single character list
    if not s or len(s) <= 1:
        return
    
    # Use two-pointer technique to swap characters
    left, right = 0, len(s) - 1
    while left < right:
        # Swap characters
        s[left], s[right] = s[right], s[left]
        
        # Move pointers towards center
        left += 1
        right -= 1