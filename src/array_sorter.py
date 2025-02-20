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
    even_nums = [num for num in sorted_arr if num % 2 == 0]
    odd_nums = [num for num in sorted_arr if num % 2 != 0]
    
    # Sort squares of even numbers in descending order
    even_squares_desc = sorted([num**2 for num in even_nums], reverse=True)
    
    # Combine the results: odd numbers first, then even number squares
    return odd_nums + even_squares_desc