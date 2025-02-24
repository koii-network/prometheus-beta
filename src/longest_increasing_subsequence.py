from typing import List, Union

def longest_increasing_subsequence(arr: List[int], return_sequence: bool = False) -> Union[int, List[int]]:
    """
    Find the longest increasing subsequence in a given array of integers.
    
    Args:
        arr (List[int]): Input array of integers
        return_sequence (bool, optional): If True, return the subsequence. 
                                          If False, return its length. 
                                          Defaults to False.
    
    Returns:
        Union[int, List[int]]: Length of the longest increasing subsequence 
                                or the subsequence itself
    
    Raises:
        TypeError: If input is not a list
        ValueError: If input list contains non-integer elements
    
    Examples:
        >>> longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60])
        5
        >>> longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60], return_sequence=True)
        [10, 22, 33, 50, 60]
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not all(isinstance(x, int) for x in arr):
        raise ValueError("All elements must be integers")
    
    # Handle empty list case
    if not arr:
        return [] if return_sequence else 0
    
    # Dynamic programming to find longest increasing subsequence
    n = len(arr)
    # Length of LIS ending at each index
    lengths = [1] * n
    # Previous element index for reconstruction
    prev = [-1] * n
    
    # Compute LIS
    max_length = 1
    max_index = 0
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and lengths[i] < lengths[j] + 1:
                lengths[i] = lengths[j] + 1
                prev[i] = j
        
        # Track the overall maximum
        if lengths[i] > max_length:
            max_length = lengths[i]
            max_index = i
    
    # Reconstruct the subsequence if needed
    if return_sequence:
        subsequence = []
        current = max_index
        while current != -1:
            subsequence.append(arr[current])
            current = prev[current]
        return list(reversed(subsequence))
    
    return max_length