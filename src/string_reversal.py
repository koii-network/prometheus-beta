def reverse_string(s: list) -> None:
    """
    Reverse a string in-place with O(1) space complexity.
    
    This function modifies the input list of characters directly,
    without creating a new list or using additional space 
    proportional to the input size.
    
    Args:
        s (list): A mutable list of characters to be reversed in-place.
    
    Time Complexity: O(n/2) = O(n), where n is the length of the string
    Space Complexity: O(1), as reversal is done using constant extra space
    
    Raises:
        TypeError: If input is not a list
    
    Examples:
        >>> chars = list('hello')
        >>> reverse_string(chars)
        >>> chars
        ['o', 'l', 'l', 'e', 'h']
    """
    # Check for invalid input
    if not isinstance(s, list):
        raise TypeError("Input must be a list of characters")
    
    # Two-pointer approach for in-place reversal
    left, right = 0, len(s) - 1
    
    while left < right:
        # Swap characters from both ends moving towards the center
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1