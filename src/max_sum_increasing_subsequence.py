from typing import List
import bisect

def max_sum_increasing_subsequence(arr: List[int]) -> int:
    """
    Find the maximum sum of an increasing subsequence with O(n log n) time complexity.
    
    Args:
        arr (List[int]): Input array of integers
    
    Returns:
        int: Maximum sum of an increasing subsequence
    
    Raises:
        ValueError: If input array is empty
    """
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    # Each index stores the max sum of increasing subsequence ending at that value
    max_sums = [arr[0]]
    # Keep track of the maximum sum found
    global_max_sum = arr[0]
    
    for num in arr[1:]:
        # Find the position where num would be inserted to maintain sorted order
        idx = bisect.bisect_left(max_sums, num)
        
        if idx == len(max_sums):
            # If num is larger than all previous max sums, append it
            if num > max_sums[-1]:
                max_sums.append(num)
                global_max_sum = max(global_max_sum, num)
        else:
            # If current number is smaller, replace the existing max_sum
            current_sum = num
            if idx > 0:
                current_sum += max_sums[idx-1]
            
            max_sums[idx] = current_sum
            global_max_sum = max(global_max_sum, current_sum)
    
    return global_max_sum