def find_max_product_consecutive_three(arr):
    """
    Find the maximum product of any three consecutive elements in the array.
    
    Args:
        arr (list): An array of integers 
    
    Returns:
        int or float: The maximum product of three consecutive elements
        
    Raises:
        ValueError: If the input array has fewer than 3 elements
    """
    # Check if array has at least 3 elements
    if len(arr) < 3:
        raise ValueError("Array must have at least 3 elements")
    
    # Initialize max_product with the product of first three elements
    max_product = arr[0] * arr[1] * arr[2]
    
    # Iterate through the array to find the maximum product
    for i in range(1, len(arr) - 2):
        # Calculate product of three consecutive elements
        current_product = arr[i] * arr[i+1] * arr[i+2]
        
        # Update max_product if current_product is larger
        max_product = max(max_product, current_product)
    
    return max_product