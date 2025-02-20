def find_odd_frequency_number(numbers):
    """
    Find the smallest number that appears an odd number of times using bitwise operations.
    
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
    
    # Find all numbers with odd frequency
    odd_frequency_numbers = []
    
    # Use a bitwise approach to find numbers with odd frequencies
    for num in numbers:
        # XOR the current number with all potential odd frequency numbers
        current_count = sum(1 for x in numbers if x == num)
        
        # If count is odd and not already in odd_frequency_numbers
        if current_count % 2 != 0 and num not in odd_frequency_numbers:
            odd_frequency_numbers.append(num)
    
    # If no numbers have odd frequency, raise an error
    if not odd_frequency_numbers:
        raise ValueError("No number appears an odd number of times")
    
    # Return the smallest number with odd frequency
    return min(odd_frequency_numbers)