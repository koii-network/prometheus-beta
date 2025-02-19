from typing import List
import bisect

def max_increasing_subsequence_sum(nums: List[int]) -> int:
    """
    Calculate the maximum sum of an increasing subsequence in O(n log n) time.
    
    Args:
        nums (List[int]): Input array of integers
    
    Returns:
        int: Maximum sum of an increasing subsequence
    
    Time complexity: O(n log n)
    Space complexity: O(n)
    """
    if not nums:
        return 0
    
    # Store the maximum sum of subsequences
    dp_sums = []
    
    for num in nums:
        # Find the insertion point to maintain increasing subsequence
        idx = bisect.bisect_left(dp_sums, num)
        
        if idx == len(dp_sums):
            # Append to the end if num is larger than all previous elements
            dp_sums.append(num)
        else:
            # Replace the element at idx to potentially create a better subsequence
            dp_sums[idx] = num
    
    # Return the maximum sum possible
    return sum(dp_sums)