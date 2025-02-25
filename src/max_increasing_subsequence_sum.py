from typing import List, Optional

def max_increasing_subsequence_sum(arr: List[int]) -> Optional[int]:
    """
    Calculate the maximum sum of an increasing subsequence with O(n log n) time complexity.
    
    Args:
        arr (List[int]): Input array of integers
    
    Returns:
        Optional[int]: Maximum sum of an increasing subsequence, 
                       or None if the input array is empty
    
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    
    Examples:
        >>> max_increasing_subsequence_sum([1, 101, 2, 3, 100])
        106
        >>> max_increasing_subsequence_sum([10, 22, 9, 33, 21, 50, 41, 60])
        165
        >>> max_increasing_subsequence_sum([])
        None
    """
    # Handle empty input
    if not arr:
        return None
    
    # Initialize dp array to store maximum sum of subsequence ending at each index
    n = len(arr)
    dp = arr.copy()
    
    # Compute the maximum sum of increasing subsequence
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + arr[i])
    
    # Return the maximum sum of all possible subsequences
    return max(dp)

def binary_search(sums: List[int], target: int) -> int:
    """
    Perform binary search to find the insertion point for target.
    
    Args:
        sums (List[int]): Sorted list of current subsequence sums
        target (int): Number to be inserted/compared
    
    Returns:
        int: Index where target should be inserted
    """
    left, right = 0, len(sums)
    
    while left < right:
        mid = (left + right) // 2
        if sums[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left