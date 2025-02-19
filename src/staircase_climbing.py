def count_staircase_ways(stair_lengths):
    """
    Calculate the number of ways to climb a staircase with given step lengths.
    
    Args:
        stair_lengths (list): A list of integers representing the lengths of stairs.
    
    Returns:
        int: The total number of unique ways to climb the staircase.
    
    Raises:
        ValueError: If stair_lengths is empty or contains non-positive integers.
    """
    # Validate input
    if not stair_lengths or any(length <= 0 for length in stair_lengths):
        raise ValueError("Stair lengths must be a non-empty list of positive integers")
    
    # Total height of the staircase
    total_height = sum(stair_lengths)
    
    # Dynamic programming array to store number of ways
    ways = [0] * (total_height + 1)
    ways[0] = 1  # Base case: one way to climb 0 height
    
    # Compute ways for each possible height
    for height in range(1, total_height + 1):
        # Can climb 1 or 2 steps at a time
        for step in (1, 2):
            if height >= step:
                ways[height] += ways[height - step]
    
    return ways[total_height]