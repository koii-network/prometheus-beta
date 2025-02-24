def find_odd_frequency_number(numbers):
    """
    Find the smallest number that appears an odd number of times in the list using bitwise XOR.
    
    Args:
        numbers (list): A list of integers
    
    Returns:
        int: The smallest number that appears an odd number of times
    
    Raises:
        ValueError: If no number appears an odd number of times or the input list is empty
    """
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    # First, use XOR to find potential odd frequency numbers
    xor_result = 0
    for num in numbers:
        xor_result ^= num
    
    # If no number appears an odd number of times, xor_result will be 0
    if xor_result == 0:
        raise ValueError("No number appears an odd number of times")
    
    # Now find the smallest number with odd frequency
    odd_frequency_candidates = [
        num for num in set(numbers) 
        if numbers.count(num) % 2 == 1
    ]
    
    if not odd_frequency_candidates:
        raise ValueError("No number appears an odd number of times")
    
    return min(odd_frequency_candidates)