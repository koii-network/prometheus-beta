def reverse_string_in_place(s: list) -> None:
    """
    Reverse a list of characters in-place with O(1) space complexity.
    
    Args:
        s (list): A list of characters to be reversed in-place.
    
    Note:
        This function modifies the input list directly and returns None.
    
    Time complexity: O(n)
    Space complexity: O(1)
    
    Examples:
        >>> chars = ['h', 'e', 'l', 'l', 'o']
        >>> reverse_string_in_place(chars)
        >>> chars
        ['o', 'l', 'l', 'e', 'h']
    """
    # Edge cases
    if not s or len(s) <= 1:
        return

    # Two-pointer approach to swap characters
    left, right = 0, len(s) - 1
    while left < right:
        # Swap characters
        s[left], s[right] = s[right], s[left]
        
        # Move pointers towards center
        left += 1
        right -= 1