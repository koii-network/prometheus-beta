def find_odd_occurrence(numbers):
    """
    Find the smallest number that appears an odd number of times using bitwise XOR.
    
    Args:
        numbers (list): A list of integers
    
    Returns:
        int: The smallest number that appears an odd number of times
    
    Raises:
        ValueError: If no number appears an odd number of times
    """
    # If the list is empty, raise an error
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    # Use a dictionary to track odd occurrences
    odd_occurrences = {}
    
    # Use bitwise XOR to find XOR of all elements
    xor_result = 0
    for num in numbers:
        # XOR for tracking
        xor_result ^= num
        
        # Count occurrences
        odd_occurrences[num] = odd_occurrences.get(num, 0) + 1
    
    # Find all numbers with odd occurrences
    odd_nums = [num for num, count in odd_occurrences.items() if count % 2 != 0]
    
    # If no odd occurrence numbers found, raise an error
    if not odd_nums:
        raise ValueError("No number appears an odd number of times")
    
    # Return the smallest number with odd occurrences
    return min(odd_nums)