def find_max_consecutive_product(arr):
    """
    Find the maximum product of any three consecutive elements in an array.
    
    Args:
        arr (list): A list of integers, can contain positive, negative, and zero values.
    
    Returns:
        int: The maximum product of three consecutive elements.
    
    Raises:
        ValueError: If the input array has fewer than 3 elements.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Check if the array has at least 3 elements
    if len(arr) < 3:
        raise ValueError("Array must contain at least 3 elements")
    
    # Initialize max product to the product of first three elements
    max_product = max(
        # First three element product
        arr[0] * arr[1] * arr[2],
        # Three consecutive elements
        max(
            # Check each three consecutive elements
            arr[i] * arr[i+1] * arr[i+2] 
            for i in range(len(arr) - 2)
        )
    )
    
    return max_product