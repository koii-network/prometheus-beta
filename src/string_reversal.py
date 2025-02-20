def reverse_string_in_place(s: list) -> None:
    """
    Reverse a string in-place using two-pointer technique.
    
    This function modifies the input list in-place, reversing its elements 
    with O(1) additional space complexity.
    
    Args:
        s (list): A list of characters to be reversed.
    
    Time Complexity: O(n), where n is the length of the string
    Space Complexity: O(1)
    """
    # Check for empty or single-character list
    if not s or len(s) <= 1:
        return
    
    # Two-pointer approach
    left, right = 0, len(s) - 1
    
    while left < right:
        # Swap characters from both ends
        s[left], s[right] = s[right], s[left]
        
        # Move pointers towards the center
        left += 1
        right -= 1