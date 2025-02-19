def find_max_product_consecutive(arr):
    """
    Find the maximum product of any three consecutive elements in the array.
    
    Args:
        arr (list): Input array of integers, can contain positive, negative, 
                    and zero values.
    
    Returns:
        int or float: Maximum product of any three consecutive elements.
        None: If the array has fewer than 3 elements.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Check if array has less than 3 elements
    if len(arr) < 3:
        return None
    
    # Initialize max product with first three elements
    max_product = arr[0] * arr[1] * arr[2]
    
    # Iterate through the array to find max product
    for i in range(1, len(arr) - 2):
        # Calculate current consecutive product
        current_product = arr[i] * arr[i+1] * arr[i+2]
        
        # Update max_product if current_product is larger
        max_product = max(max_product, current_product)
    
    return max_product