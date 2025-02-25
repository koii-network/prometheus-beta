from typing import List, Optional

def find_max_consecutive_product(arr: List[int]) -> Optional[int]:
    """
    Find the maximum product of any three consecutive elements in the array.
    
    Args:
        arr (List[int]): Input array of integers
    
    Returns:
        Optional[int]: Maximum product of three consecutive elements, 
                       or None if array is too short
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Handles:
    - Arrays with positive and negative integers
    - Arrays containing zero
    - Arrays with different length scenarios
    """
    # Check if array has less than 3 elements
    if len(arr) < 3:
        return None
    
    # Initialize max product
    max_product = float('-inf')
    
    # Check all possible consecutive 3-element subsets
    for i in range(len(arr) - 2):
        # Skip cases involving zero if possible
        if arr[i] == 0 or arr[i+1] == 0 or arr[i+2] == 0:
            subset_product = 0
        else:
            subset_product = arr[i] * arr[i+1] * arr[i+2]
        
        # Update max product
        max_product = max(max_product, subset_product)
    
    return max_product if max_product != float('-inf') else None