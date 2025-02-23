def multiply(arr):
    """
    Multiply corresponding elements of input arrays.

    Args:
        arr (list): A list of lists of numbers to multiply.

    Returns:
        list: A new list where each element is the product of 
              corresponding elements from input arrays.

    Raises:
        TypeError: If input is not a list of lists.
        ValueError: If lists are empty or have mismatched lengths.
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of lists")
    
    # Check if input is empty
    if not arr:
        raise ValueError("Input must be a non-empty list of lists")
    
    # Check if all elements are lists
    if not all(isinstance(sublist, list) for sublist in arr):
        raise TypeError("Input must be a list of lists")
    
    # Check if lists are non-empty
    if any(len(sublist) == 0 for sublist in arr):
        raise ValueError("All input lists must be non-empty")
    
    # Check if all elements are numeric
    if not all(all(isinstance(x, (int, float)) for x in sublist) for sublist in arr):
        raise TypeError("All elements must be numeric")
    
    # Check if all lists have the same length
    if len(set(len(sublist) for sublist in arr)) > 1:
        raise ValueError("All input lists must have the same length")
    
    # Multiply corresponding elements
    return [
        # Multiply all elements at the same index across all input lists
        multiply_list(index, arr) 
        for index in range(len(arr[0]))
    ]

def multiply_list(index, arr):
    """
    Multiply elements at a specific index across all input lists.

    Args:
        index (int): Index to multiply.
        arr (list): List of lists of numbers.

    Returns:
        number: Product of elements at the given index.
    """
    result = 1
    for sublist in arr:
        result *= sublist[index]
    return result