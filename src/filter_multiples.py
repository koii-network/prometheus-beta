def filter_unique_multiples(numbers):
    """
    Filter a list of integers to include only numbers that are multiples of 3 or 5, but not both.
    
    Args:
        numbers (list): A list of integers to filter.
    
    Returns:
        list: A sorted list of integers that are multiples of 3 or 5, but not both.
    """
    def is_unique_multiple(num):
        # Check if number is multiple of 3 XOR multiple of 5
        return (num % 3 == 0) != (num % 5 == 0)
    
    # Filter unique multiples and sort in ascending order
    return sorted(list(filter(is_unique_multiple, numbers)))