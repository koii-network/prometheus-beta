def sum_array(arr):
    """
    Calculate the sum of elements in an input array of integers.

    Args:
        arr (list): A list of integers to be summed.

    Returns:
        int: The sum of all elements in the input array.

    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if all elements are integers
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("All elements must be integers")
    
    # Return the sum of the array
    return sum(arr)