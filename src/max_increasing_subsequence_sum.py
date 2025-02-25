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
    
    # Store the maximum sums of subsequences
    max_sums = []
    
    for num in arr:
        # Find the insertion point for the current number
        insert_idx = binary_search(max_sums, num)
        
        # If the number can't be added to an existing subsequence
        if insert_idx == len(max_sums):
            max_sums.append(num)
        else:
            # Update the current subsequence sum
            if insert_idx == 0:
                max_sums[insert_idx] = num
            else:
                max_sums[insert_idx] = max(max_sums[insert_idx], 
                                           max_sums[insert_idx - 1] + num)
    
    return max(max_sums)

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