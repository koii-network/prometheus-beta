def find_max_consecutive_product(arr):
    """
    Find the maximum product of any three consecutive elements in an array.
    
    Args:
        arr (list): An array of integers, potentially containing positive, 
                    negative numbers, and zeros.
    
    Returns:
        int or float: The maximum product of three consecutive elements.
        
    Raises:
        ValueError: If the input array has fewer than 3 elements.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Check if array has at least 3 elements
    if len(arr) < 3:
        raise ValueError("Array must contain at least 3 elements")
    
    # Initialize max product with first three elements
    max_product = arr[0] * arr[1] * arr[2]
    
    # Iterate through the array to find max consecutive product
    for i in range(1, len(arr) - 2):
        current_product = arr[i] * arr[i+1] * arr[i+2]
        max_product = max(max_product, current_product)
    
    return max_product