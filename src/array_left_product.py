def product_of_left_elements(arr):
    """
    Returns an array where each element is the product of numbers to its left.
    
    Args:
        arr (list): Input list of numbers
    
    Returns:
        list: Array with product of left elements for each position
    
    Examples:
        [3, 1, 2, 5, 4] -> [1, 3, 3, 6, 30]
        [2, 4, 6, 8] -> [1, 2, 8, 48]
    """
    if not arr:
        return []
    
    result = [1] * len(arr)
    left_product = 1
    
    for i in range(len(arr)):
        result[i] = left_product
        left_product *= arr[i]
    
    return result