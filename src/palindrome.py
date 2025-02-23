def is_palindrome(arr):
    """
    Determine if a list of integers is a palindrome.
    
    A palindrome reads the same backward as forward.
    
    Args:
        arr (list): A list of integers to check
    
    Returns:
        bool: True if the list is a palindrome, False otherwise
    
    Raises:
        TypeError: If input is not a list
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Empty list or list with one element is a palindrome
    if len(arr) <= 1:
        return True
    
    # Compare elements from start and end, moving inwards
    left = 0
    right = len(arr) - 1
    
    while left < right:
        if arr[left] != arr[right]:
            return False
        left += 1
        right -= 1
    
    return True