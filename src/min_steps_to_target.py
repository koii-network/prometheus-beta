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
    
    # Check all possible combinations of addition and subtraction
    for steps in range(1, n + 1):
        for combo in combinations(range(n), steps):
            current_sum = 0
            used_indices = set()
            
            # Try positive additions first
            for idx in combo:
                if idx not in used_indices:
                    current_sum += nums[idx]
                    used_indices.add(idx)
            
            if current_sum == target:
                return steps
            
            # If not found, try with some numbers subtracted
            for sub_count in range(1, steps + 1):
                for subtract_combo in combinations(combo, sub_count):
                    reset_sum = 0
                    reset_indices = set()
                    
                    for idx in combo:
                        if idx not in reset_indices:
                            if idx in subtract_combo:
                                reset_sum -= nums[idx]
                            else:
                                reset_sum += nums[idx]
                            reset_indices.add(idx)
                    
                    if reset_sum == target:
                        return steps
    
    return -1  # Cannot reach target sum