def find_smallest_int_to_multiple_of_five(arr):
    """
    Find the smallest positive integer that, when added to the sum of all numbers 
    in the array, results in a multiple of 5.
    
    Args:
        arr (list): A list of integers
    
    Returns:
        int: The smallest positive integer that makes the sum a multiple of 5
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-integer elements
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if all elements are integers
    if not all(isinstance(x, int) for x in arr):
        raise ValueError("All elements must be integers")
    
    # Calculate the current sum of the array
    current_sum = sum(arr)
    
    # Find the smallest positive integer to make the sum a multiple of 5
    remainder = current_sum % 5
    
    # Calculate the number to add to make sum a multiple of 5
    if remainder == 0:
        return 5
    
    return 5 - remainder