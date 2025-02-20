def sort_array_with_even_squares(arr):
    """
    Sort the input array in ascending order, 
    then sort even number squares in descending order.
    
    Args:
        arr (list): Input list of numbers
    
    Returns:
        list: Sorted array with even number squares in descending order
    """
    if not arr:
        return []
    
    # Sort the entire array in ascending order
    sorted_arr = sorted(arr)
    
    # Separate even and odd numbers
    even_nums = [num for num in sorted_arr if num % 2 == 0]
    odd_nums = [num for num in sorted_arr if num % 2 != 0]
    
    # Sort even number squares in descending order
    even_nums_sorted = sorted(even_nums, key=lambda x: x**2, reverse=True)
    
    # Combine the lists
    return odd_nums + even_nums_sorted