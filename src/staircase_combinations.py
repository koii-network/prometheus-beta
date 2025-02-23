def calculate_staircase_combinations(stair_lengths):
    """
    Calculate the number of ways to climb a staircase with given step lengths.
    
    :param stair_lengths: List of step lengths representing the total staircase
    :return: Number of unique ways to climb the staircase using 1 or 2 steps
    :raises ValueError: If stair_lengths is empty or contains non-positive integers
    """
    # Validate input
    if not stair_lengths:
        raise ValueError("Stair lengths list cannot be empty")
    
    if any(length <= 0 for length in stair_lengths):
        raise ValueError("All stair lengths must be positive integers")
    
    # Recursive helper function with memoization
    def climb_stairs(current_index, total_climb):
        # Base cases
        if total_climb == 0:
            return 1
        if total_climb < 0 or current_index >= len(stair_lengths):
            return 0
        
        # Memoization key
        key = (current_index, total_climb)
        
        # Check memoized result
        if key in memo:
            return memo[key]
        
        # Recursive calls for 1 and 2 step possibilities
        ways = (
            climb_stairs(current_index, total_climb - 1) +  # 1-step climb
            climb_stairs(current_index, total_climb - 2)    # 2-step climb
        )
        
        # Memoize and return
        memo[key] = ways
        return ways
    
    # Memoization dictionary to store computed results
    memo = {}
    
    # Calculate total stairs
    total_stairs = sum(stair_lengths)
    
    # Start climbing from different points to cover all combinations
    total_combinations = 0
    for start_point in range(len(stair_lengths)):
        total_combinations += climb_stairs(start_point, total_stairs)
    
    return total_combinations