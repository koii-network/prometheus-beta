def sort_array_with_even_squares(arr):
    """
    Sort an array in ascending order, with even numbers squared and sorted in descending order.
    
    Args:
        arr (list): Input list of numbers
    
    Returns:
        list: Sorted array with even numbers squared and sorted in descending order
    
    Raises:
        TypeError: If input is not a list
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # If list is empty, return empty list
    if not arr:
        return []
    
    # Create a copy of the input list to avoid modifying the original
    sorted_arr = sorted(arr)
    
    # Separate even and odd numbers while maintaining order
    even_nums = [num for num in sorted_arr if num % 2 == 0]
    odd_nums = [num for num in sorted_arr if num % 2 != 0]
    
    # Square the even numbers and sort in descending order
    squared_even_nums = sorted([num**2 for num in even_nums], reverse=True)
    
    # Combine lists: odd numbers first (sorted), then squared even numbers sorted in descending order
    return odd_nums + squared_even_nums