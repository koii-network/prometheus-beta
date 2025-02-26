def count_matching_elements(arr1, arr2):
    """
    Count the number of elements in the first array that are also present in the second array.

    Args:
        arr1 (list): The first array of integers to check.
        arr2 (list): The second array of integers to compare against.

    Returns:
        int: The number of elements from arr1 that are also in arr2.

    Raises:
        TypeError: If either input is not a list or contains non-integer elements.
    """
    # Validate input types
    if not isinstance(arr1, list) or not isinstance(arr2, list):
        raise TypeError("Both arguments must be lists")
    
    # Validate list contents
    if not all(isinstance(x, int) for x in arr1 + arr2):
        raise TypeError("All elements must be integers")
    
    # Convert arr2 to a set for O(1) lookup
    arr2_set = set(arr2)
    
    # Count matching elements
    return sum(1 for x in arr1 if x in arr2_set)