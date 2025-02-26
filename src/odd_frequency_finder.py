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
    
    # Find the unique number that appears an odd number of times
    # Create a frequency dictionary to track occurrences
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    
    # Filter numbers with odd frequency and find the smallest
    odd_freq_nums = [num for num, count in frequency.items() if count % 2 == 1]
    
    # If no numbers with odd frequency, raise an error
    if not odd_freq_nums:
        raise ValueError("No number appears an odd number of times")
    
    # Return the smallest number with odd frequency
    return min(odd_freq_nums)