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
    
    # Track max possible product
    max_product = float('-inf')
    
    # Iterate through the array to find max product
    for i in range(len(arr) - 2):
        # Calculate current consecutive product
        current_product = arr[i] * arr[i+1] * arr[i+2]
        
        # Update max product 
        max_product = max(max_product, current_product)
    
    return max_product if max_product != float('-inf') else None