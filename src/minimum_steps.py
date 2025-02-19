from typing import List

def minimum_steps_to_target(numbers: List[int], target: int) -> int:
    """
    Calculate the minimum number of steps to reach target sum using each number once.
    
    Args:
        numbers (List[int]): List of integers to use
        target (int): Target sum to reach
    
    Returns:
        int: Minimum number of steps to reach target, or -1 if impossible
    """
    def backtrack(current_sum: int, index: int, steps: int) -> int:
        # Base case: reached target sum
        if current_sum == target:
            return steps
        
        # If we've gone through all numbers or exceeded possible steps
        if index >= len(numbers):
            return float('inf')
        
        # Try adding the current number
        add_result = backtrack(current_sum + numbers[index], index + 1, steps + 1)
        
        # Try subtracting the current number 
        subtract_result = backtrack(current_sum - numbers[index], index + 1, steps + 1)
        
        # Return the minimum of the two paths
        return min(add_result, subtract_result)
    
    # Start the backtracking process
    result = backtrack(0, 0, 0)
    
    # Return -1 if no solution was found
    return result if result != float('inf') else -1