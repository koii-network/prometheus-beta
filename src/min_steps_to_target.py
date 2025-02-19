from typing import List
from itertools import combinations

def min_steps_to_target_sum(nums: List[int], target: int) -> int:
    """
    Calculate the minimum number of steps to reach the target sum using each number once.
    
    Args:
        nums (List[int]): List of integers to use
        target (int): Target sum to reach
    
    Returns:
        int: Minimum number of steps, or -1 if target cannot be reached
    """
    n = len(nums)
    
    # If no numbers, impossible to reach target
    if not nums:
        return -1
    
    # Check all possible combinations of numbers and operations
    for steps in range(1, n + 1):
        for combo in combinations(range(n), steps):
            # Explore all possible sign combinations with dynamic bit manipulation
            for mask in range(1, 2**steps):
                current_sum = 0
                used_indices = set()
                
                for j, idx in enumerate(combo):
                    if idx not in used_indices:
                        # Dynamic sign based on bit mask
                        sign = 1 if mask & (1 << j) else -1
                        current_sum += sign * nums[idx]
                        used_indices.add(idx)
                
                if current_sum == target:
                    return steps
    
    return -1  # Cannot reach target sum