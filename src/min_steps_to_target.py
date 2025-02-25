from typing import List

def min_steps_to_target_sum(numbers: List[int], target: int) -> int:
    """
    Calculate the minimum number of steps to reach a target sum using given numbers.
    
    Each number can be used only once, and steps can involve addition or subtraction.
    
    Args:
        numbers (List[int]): A list of integers to use for reaching the target
        target (int): The target sum to reach
    
    Returns:
        int: Minimum number of steps to reach the target sum, or -1 if impossible
    
    Raises:
        ValueError: If input list is empty
    """
    # Validate input
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    # Use dynamic programming to solve the problem
    # Track unique combinations of current sum and used numbers
    n = len(numbers)
    
    # Use a set to store unique states: (current_sum, used_numbers_mask)
    states = {(0, 0)}
    
    # Track minimum steps
    min_steps = float('inf')
    
    # Try all possible combinations
    for steps in range(1, n + 1):
        new_states = set()
        
        for current_sum, used_mask in states:
            for i in range(n):
                # Skip if number already used
                if used_mask & (1 << i):
                    continue
                
                # Try adding the number
                add_sum = current_sum + numbers[i]
                add_mask = used_mask | (1 << i)
                if add_sum == target:
                    min_steps = min(min_steps, steps)
                new_states.add((add_sum, add_mask))
                
                # Try subtracting the number
                sub_sum = current_sum - numbers[i]
                sub_mask = used_mask | (1 << i)
                if sub_sum == target:
                    min_steps = min(min_steps, steps)
                new_states.add((sub_sum, sub_mask))
        
        states = new_states
    
    # Return result
    return min_steps if min_steps != float('inf') else -1