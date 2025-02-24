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
    
    # Separate even and odd numbers, track their original positions
    even_positions = [(i, num) for i, num in enumerate(sorted_arr) if num % 2 == 0]
    odd_positions = [(i, num) for i, num in enumerate(sorted_arr) if num % 2 != 0]
    
    # Create sorted even squares
    even_squares = sorted([(pos[0], pos[1] ** 2) for pos in even_positions], key=lambda x: x[1], reverse=True)
    
    # Combine odd and sorted squares back into the original array
    result = [0] * len(sorted_arr)
    
    # First place odd numbers
    for pos, val in odd_positions:
        result[pos] = val
    
    # Then place even squares
    for (orig_pos, square) in even_squares:
        result[orig_pos] = square
    
    return result