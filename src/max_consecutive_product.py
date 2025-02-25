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
    
    # Initialize max product with first three elements
    max_prod = arr[0] * arr[1] * arr[2]
    
    # Slide a window of 3 elements and track max product
    for i in range(1, len(arr) - 2):
        current_prod = arr[i] * arr[i+1] * arr[i+2]
        max_prod = max(max_prod, current_prod)
    
    return max_prod