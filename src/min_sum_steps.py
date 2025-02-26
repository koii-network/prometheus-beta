from typing import List

def min_steps_to_target_sum(numbers: List[int], target_sum: int) -> int:
    """
    Calculate the minimum number of steps to reach the target sum using the given list of numbers.
    
    Each number can be used only once, and steps can involve addition or subtraction.
    
    Args:
        numbers (List[int]): List of integers to use for reaching the target sum
        target_sum (int): The target sum to reach
    
    Returns:
        int: Minimum number of steps to reach the target sum, or -1 if impossible
    """
    # Create a dynamic programming cache to store minimum steps
    from functools import lru_cache
    
    @lru_cache(maxsize=None)
    def dp(remaining_sum, index):
        # Base cases
        if remaining_sum == 0:
            return 0
        
        # Out of numbers and sum not zero
        if index >= len(numbers):
            return float('inf')
        
        # Try both adding and subtracting current number
        add_steps = float('inf')
        sub_steps = float('inf')
        
        # Skip the current number
        skip_steps = dp(remaining_sum, index + 1)
        
        # Try adding the current number
        if abs(remaining_sum - numbers[index]) < abs(remaining_sum):
            add_steps = 1 + dp(remaining_sum - numbers[index], index + 1)
        
        # Try subtracting the current number
        if abs(remaining_sum + numbers[index]) < abs(remaining_sum):
            sub_steps = 1 + dp(remaining_sum + numbers[index], index + 1)
        
        # Return minimum of all possible steps
        return min(skip_steps, add_steps, sub_steps)
    
    # Compute minimum steps
    result = dp(target_sum, 0)
    
    # Return -1 if no solution found
    return result if result != float('inf') else -1