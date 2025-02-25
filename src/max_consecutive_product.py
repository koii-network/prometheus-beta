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
    
    # Helper function to get max of multiple products
    def compare_products(*products):
        return max(products)
    
    # Special cases for small arrays
    if len(arr) == 3:
        return arr[0] * arr[1] * arr[2]
    
    # Initialize max product with carefully considering signs
    first_max = compare_products(
        arr[0] * arr[1] * arr[2],  # First three
        arr[0] * arr[1] * arr[3],  # First two and next
        arr[0] * arr[2] * arr[3],  # First, third and next
        arr[1] * arr[2] * arr[3]   # Next three
    )
    
    # Track max product as we iterate
    current_max = first_max
    
    # Iterate through the array to find max consecutive product
    for i in range(1, len(arr) - 2):
        # Consider three consecutive and mixed cases
        current_product = compare_products(
            arr[i] * arr[i+1] * arr[i+2],  # Three consecutive
            arr[i-1] * arr[i] * arr[i+1],  # Sliding window left
            arr[i+1] * arr[i+2] * arr[i+3]  # Sliding window right
        )
        current_max = max(current_max, current_product)
    
    return current_max