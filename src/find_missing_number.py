def find_missing_number(nums):
    """
    Find the missing number in an array of integers from 1 to n+1.
    
    Args:
        nums (list): A list of integers containing unique numbers from 1 to n+1, 
                     with one number missing.
    
    Returns:
        int: The missing number from the sequence.
    
    Raises:
        ValueError: If the input is not a valid list of integers or is empty.
        ValueError: If the list does not represent a continuous sequence with one missing number.
    
    Example:
        >>> find_missing_number([1, 3, 4, 5])
        2
        >>> find_missing_number([2, 3, 4, 5, 6])
        1
    """
    # Validate input
    if not nums or not isinstance(nums, list):
        raise ValueError("Input must be a non-empty list of integers")
    
    # Convert to a set for O(1) lookup
    num_set = set(nums)
    
    # Find the range of expected numbers 
    # The range is from 1 to len(nums) + 1
    for num in range(1, len(nums) + 2):
        if num not in num_set:
            return num
    
    # This should never happen if input is valid
    raise ValueError("No missing number found in the sequence")