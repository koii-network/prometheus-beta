def sort_array_with_even_squares(arr):
    """
    Sort the input array in ascending order, 
    then sort even number squares in descending order.
    
    Args:
        arr (list): Input list of numbers
    
    Returns:
        list: Sorted array with even number squares sorted in descending order
    """
    if not arr:
        return []
    
    # Sort the entire array in ascending order
    sorted_arr = sorted(arr)
    
    # Separate even and odd numbers
    even_squares = [x**2 for x in sorted_arr if x % 2 == 0]
    odd_numbers = [x for x in sorted_arr if x % 2 != 0]
    
    # Sort even squares in descending order
    even_squares.sort(reverse=True)
    
    # Combine odd numbers (in ascending order) with even squares (in descending order)
    return odd_numbers + even_squares