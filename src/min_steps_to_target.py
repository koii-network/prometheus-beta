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
    
    # Use a dictionary to store states with their minimum steps
    states = {(0, 0): 0}
    
    # Track minimum steps
    min_steps = float('inf')
    
    # Try all possible combinations
    for steps in range(1, n + 1):
        new_states = {}
        
        for (current_sum, used_mask), current_steps in states.items():
            for i in range(n):
                # Skip if number already used
                if used_mask & (1 << i):
                    continue
                
                # Try adding the number
                add_sum = current_sum + numbers[i]
                add_mask = used_mask | (1 << i)
                if add_sum == target:
                    min_steps = min(min_steps, steps)
                new_states[(add_sum, add_mask)] = min(
                    new_states.get((add_sum, add_mask), float('inf')), 
                    steps
                )
                
                # Try subtracting the number
                sub_sum = current_sum - numbers[i]
                sub_mask = used_mask | (1 << i)
                if sub_sum == target:
                    min_steps = min(min_steps, steps)
                new_states[(sub_sum, sub_mask)] = min(
                    new_states.get((sub_sum, sub_mask), float('inf')), 
                    steps
                )
        
        states = new_states
    
    # Return result
    return min_steps if min_steps != float('inf') else -1