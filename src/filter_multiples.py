def filter_multiples_3_or_5(numbers):
    """
    Filter a list of integers to return only those that are multiples of 3 or 5, but not both.
    
    Args:
        numbers (list): A list of integers to filter
    
    Returns:
        list: Sorted list of integers that are multiples of 3 or 5, but not both
    """
    def is_exclusive_multiple(num):
        # Check if num is multiple of 3 XOR multiple of 5
        return (num % 3 == 0) != (num % 5 == 0)
    
    filtered_nums = [num for num in numbers if is_exclusive_multiple(num)]
    return sorted(filtered_nums)