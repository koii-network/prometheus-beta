def filter_special_multiples(numbers):
    """
    Filter a list of integers to include only numbers that are multiples 
    of either 3 or 5, but not both.
    
    Args:
        numbers (list): List of integers to filter
    
    Returns:
        list: Sorted list of integers that are multiples of 3 or 5, but not both
    """
    def is_special_multiple(num):
        # Check if number is multiple of 3 XOR multiple of 5
        return (num % 3 == 0) != (num % 5 == 0)
    
    # Filter and sort the result
    return sorted(list(filter(is_special_multiple, numbers)))