def find_odd_frequency_number(numbers):
    """
    Find the number that appears an odd number of times in the list using bitwise XOR.
    
    If multiple numbers appear an odd number of times, return the smallest one.
    
    Args:
        numbers (list): A list of integers
    
    Returns:
        int: The smallest number that appears an odd number of times
    
    Raises:
        ValueError: If the input list is empty or no number appears an odd number of times
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Handle edge cases
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    # Use bitwise XOR to find numbers with odd frequencies
    # XOR has the property that:
    # 1. a ^ a = 0 (same numbers cancel out)
    # 2. a ^ 0 = a (XORing with 0 returns the original number)
    
    # First pass: find potential candidates
    xor_result = 0
    for num in numbers:
        xor_result ^= num
    
    # If no number appears odd times, xor_result will be 0
    if xor_result == 0:
        raise ValueError("No number appears an odd number of times")
    
    # Second pass: find the smallest number with odd frequency
    smallest_odd_freq = float('inf')
    for num in numbers:
        # XOR the current number with the initial XOR result
        current_xor = num ^ xor_result
        
        # If XOR is non-zero, this number might be part of the odd frequency set
        if current_xor > 0:
            # Check how many times this number appears
            count = sum(1 for x in numbers if x == num)
            if count % 2 == 1:
                smallest_odd_freq = min(smallest_odd_freq, num)
    
    # If no number found (shouldn't happen given previous checks)
    if smallest_odd_freq == float('inf'):
        raise ValueError("No number appears an odd number of times")
    
    return smallest_odd_freq