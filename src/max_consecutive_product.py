def find_max_consecutive_product(arr):
    """
    Find the maximum product of any three consecutive elements in the array.
    
    Args:
        arr (list): A list of integers, which may contain positive, negative, 
                    and zero values.
    
    Returns:
        int or float: The maximum product of three consecutive elements.
        
    Raises:
        ValueError: If the input array has fewer than 3 elements.
    """
    # Check if the array has at least 3 elements
    if len(arr) < 3:
        raise ValueError("Array must contain at least 3 elements")
    
    # Initialize the max product with the product of first three elements
    max_product = arr[0] * arr[1] * arr[2]
    
    # Iterate through the array to find the maximum product
    for i in range(1, len(arr) - 2):
        # Calculate the product of three consecutive elements
        current_product = arr[i] * arr[i+1] * arr[i+2]
        
        # Update max_product if current_product is larger
        max_product = max(max_product, current_product)
    
    return max_product