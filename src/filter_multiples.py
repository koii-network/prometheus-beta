def filter_special_multiples(numbers):
    """
    Filter a list of integers to return numbers that are multiples of either 3 or 5, but not both.
    
    Args:
        numbers (list): A list of integers to filter
    
    Returns:
        list: Sorted list of integers that are multiples of 3 or 5, but not both
    """
    def is_special_multiple(num):
        """Check if a number is a multiple of 3 or 5, but not both."""
        is_multiple_of_3 = num % 3 == 0
        is_multiple_of_5 = num % 5 == 0
        return (is_multiple_of_3 or is_multiple_of_5) and not (is_multiple_of_3 and is_multiple_of_5)
    
    return sorted(list(filter(is_special_multiple, numbers)))