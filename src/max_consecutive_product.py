from typing import List

def max_consecutive_product(arr: List[int]) -> int:
    """
    Find the maximum product of any three consecutive elements in an array.
    
    Args:
        arr (List[int]): Input array of integers (both positive and negative)
    
    Returns:
        int: Maximum product of three consecutive elements
    
    Raises:
        ValueError: If input array has fewer than 3 elements
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Check for valid input
    if not arr or len(arr) < 3:
        raise ValueError("Input array must contain at least 3 elements")
    
    # Compute all possible consecutive products
    products = [
        # All three elements
        arr[i] * arr[i+1] * arr[i+2] 
        for i in range(len(arr) - 2)
    ]
    
    # Return the maximum of all consecutive products
    return max(products)