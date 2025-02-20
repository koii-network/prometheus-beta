def sort_array_with_even_squares(arr):
    """
    Sort the input array in ascending order, 
    then sort even number squares in descending order.
    
    Args:
        arr (list): Input list of numbers
    
    Returns:
        list: Sorted array with even number squares sorted in descending order
    """
    # If input is empty or None, return an empty list
    if not arr:
        return []
    
    # Sort the entire array in ascending order
    sorted_arr = sorted(arr)
    
    # Separate even and odd numbers
    even_nums = [num for num in sorted_arr if num % 2 == 0]
    odd_nums = [num for num in sorted_arr if num % 2 != 0]
    
    # Sort even number squares in descending order
    even_squares_sorted = sorted([num**2 for num in even_nums], reverse=True)
    
    # Reconstruct the final array
    # First, replace even numbers with their sorted squared values
    result = []
    even_square_index = 0
    
    for num in sorted_arr:
        if num % 2 == 0:
            result.append(even_squares_sorted[even_square_index])
            even_square_index += 1
        else:
            result.append(num)
    
    return result