def sort_array_with_even_squares(arr):
    """
    Sort an array in ascending order with a special handling for even number squares.
    
    Args:
        arr (list): Input list of numbers to be sorted.
    
    Returns:
        list: Sorted array with even number squares sorted in descending order.
    
    Raises:
        TypeError: If input is not a list.
    """
    # Validate input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # If list is empty, return empty list
    if not arr:
        return []
    
    # Create a copy of the input list to avoid modifying the original
    sorted_arr = sorted(arr)
    
    # Separate even and odd numbers
    even_squares = [num ** 2 for num in sorted_arr if num % 2 == 0]
    
    # Sort even squares in descending order
    even_squares.sort(reverse=True)
    
    # Create the final result
    result = []
    even_square_index = 0
    
    for num in sorted_arr:
        if num % 2 == 0:
            # Replace even numbers with their sorted squares
            result.append(even_squares[even_square_index])
            even_square_index += 1
        else:
            # Keep odd numbers in their original sorted position
            result.append(num)
    
    return result