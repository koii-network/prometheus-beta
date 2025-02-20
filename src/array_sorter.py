def sort_array_with_even_squares(arr):
    """
    Sort the input array in ascending order, 
    then sort the even number squares in descending order.
    
    Args:
        arr (list): Input list of numbers
    
    Returns:
        list: Sorted array with even squared numbers in descending order
    """
    if not arr:
        return []
    
    # Sort the original array in ascending order
    sorted_arr = sorted(arr)
    
    # Separate even and odd numbers
    even_nums = [num for num in sorted_arr if num % 2 == 0]
    odd_nums = [num for num in sorted_arr if num % 2 != 0]
    
    # Sort squares of even numbers in descending order
    even_squares = sorted([num**2 for num in even_nums], reverse=True)
    
    # Combine odd numbers (in original ascending order) with squared even numbers
    return odd_nums + even_squares