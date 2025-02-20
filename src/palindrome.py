def is_palindrome(nums):
    """
    Determine if a list of integers is a palindrome.
    
    A palindrome reads the same backward as forward.
    
    Args:
        nums (list): A list of integers
    
    Returns:
        bool: True if the list is a palindrome, False otherwise
    
    Raises:
        TypeError: If the input is not a list
    """
    # Check if input is a list
    if not isinstance(nums, list):
        raise TypeError("Input must be a list")
    
    # Compare the list with its reverse
    return nums == nums[::-1]