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
    
    # Create new lists to store odd and even numbers
    odd_nums = sorted([num for num in arr if num % 2 != 0])
    even_nums = sorted([num for num in arr if num % 2 == 0])
    
    # Calculate squares of even numbers in descending order
    even_squares = sorted([num ** 2 for num in even_nums], reverse=True)
    
    # Reconstruct the result using manual mapping
    result = []
    odd_cursor = 0
    even_square_cursor = 0
    
    for num in sorted(arr):
        if num % 2 != 0:
            # Place odd numbers first
            result.append(odd_nums[odd_cursor])
            odd_cursor += 1
        else:
            # Place even squares in descending order
            result.append(even_squares[even_square_cursor])
            even_square_cursor += 1
    
    return result