def find_odd_frequency_number(numbers):
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
    
    # Use a set to track numbers with odd frequencies
    odd_frequency_numbers = set()
    
    # Iterate through the numbers to find odd frequency numbers
    for num in numbers:
        # Use XOR to toggle tracking of odd/even occurrences
        if num in odd_frequency_numbers:
            odd_frequency_numbers.remove(num)
        else:
            odd_frequency_numbers.add(num)
    
    # If no odd frequency numbers found, raise an error
    if not odd_frequency_numbers:
        raise ValueError("No number appears an odd number of times")
    
    # Return the smallest number with odd frequency
    return min(odd_frequency_numbers)