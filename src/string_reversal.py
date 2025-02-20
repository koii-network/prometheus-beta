def reverse_string_in_place(s: list) -> None:
    """
    Reverse a string in-place with O(1) space complexity.
    
    Args:
        s (list): A list of characters to be reversed in-place.
    
    Note:
        - Modifies the input list directly
        - Time complexity: O(n)
        - Space complexity: O(1)
    """
    # Check for empty or single-character strings
    if not s or len(s) <= 1:
        return

    # Two-pointer approach to swap characters
    left, right = 0, len(s) - 1
    while left < right:
        # Swap characters
        s[left], s[right] = s[right], s[left]
        
        # Move pointers towards the center
        left += 1
        right -= 1