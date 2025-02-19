def max_product_consecutive_three(arr):
    """
    Find the maximum product of any three consecutive elements in the array.
    
    Args:
        arr (list): An array of integers (can be positive, negative, or zero)
    
    Returns:
        int or float: The maximum product of three consecutive elements
    
    Raises:
        ValueError: If the input array has fewer than 3 elements
    """
    # Check if array has at least 3 elements
    if len(arr) < 3:
        raise ValueError("Array must have at least 3 elements")
    
    # Initialize max product with the product of first 3 elements
    max_product = float('-inf')
    
    # Iterate through the array, calculating consecutive 3-element products
    for i in range(len(arr) - 2):
        # Calculate product of current 3 consecutive elements
        current_product = arr[i] * arr[i+1] * arr[i+2]
        
        # Update max_product if current product is larger
        max_product = max(max_product, current_product)
    
    return max_product