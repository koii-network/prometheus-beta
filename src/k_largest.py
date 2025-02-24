from typing import List

def k_largest(arr: List[int], k: int) -> List[int]:
    """
    Return the k largest elements from the input array.

    Args:
        arr (List[int]): Input list of integers
        k (int): Number of largest elements to return

    Returns:
        List[int]: k largest elements in descending order

    Raises:
        ValueError: If k is negative or larger than the array length
        TypeError: If input is not a list or contains non-integer elements
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if all elements are integers
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("All elements must be integers")
    
    # Validate k
    if k < 0:
        raise ValueError("k cannot be negative")
    
    if k > len(arr):
        raise ValueError("k cannot be larger than the array length")
    
    # If k is 0, return empty list
    if k == 0:
        return []
    
    # Sort in descending order and return k largest
    return sorted(arr, reverse=True)[:k]