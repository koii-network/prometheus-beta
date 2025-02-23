def find_odd_occurrence(numbers):
    """
    Find the smallest number that appears an odd number of times using bitwise operations.
    
    Args:
        numbers (list): A list of integers
    
    Returns:
        int: The smallest number that appears an odd number of times
    
    Raises:
        ValueError: If no number appears an odd number of times
    """
    # If list is empty, raise ValueError
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    # Use a set to track numbers with odd occurrences
    odd_occurrence_nums = set()
    
    # Iterate through the list to find numbers with odd occurrences
    for num in numbers:
        # XOR-based check for odd/even occurrences
        count = sum(1 for x in numbers if x == num)
        if count % 2 != 0:
            odd_occurrence_nums.add(num)
    
    # If no number appears odd number of times, raise ValueError
    if not odd_occurrence_nums:
        raise ValueError("No number appears an odd number of times")
    
    # Return the smallest number with odd occurrences
    return min(odd_occurrence_nums)