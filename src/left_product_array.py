def left_product_array(arr):
    """
    Takes an array of numbers and returns an array where each element 
    is the product of the numbers to the left of the corresponding 
    element in the original array, excluding the current element itself.
    
    Args:
        arr (list): Input list of numbers
    
    Returns:
        list: Array of left products
    
    Examples:
        >>> left_product_array([1, 2, 3, 4])
        [1, 1, 2, 6]
        >>> left_product_array([])
        []
        >>> left_product_array([5])
        [1]
    """
    # Handle empty or single-element arrays
    if len(arr) <= 1:
        return [1] if arr else []
    
    # Initialize result array and left product tracking
    result = [1] * len(arr)
    left_product = 1
    
    # Calculate left products from left to right
    for i in range(len(arr)):
        # Current result is the product of numbers to the left
        result[i] = left_product
        # Update left product for next iteration
        left_product *= arr[i]
    
    return result