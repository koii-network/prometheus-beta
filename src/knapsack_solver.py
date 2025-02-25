from typing import List, Tuple, Optional

def solve_knapsack(items: List[Tuple[int, int]], max_weight: int) -> List[Tuple[int, int]]:
    """
    Solve the 0/1 Knapsack Problem using dynamic programming.
    
    Args:
        items (List[Tuple[int, int]]): List of (weight, value) tuples representing items
        max_weight (int): Maximum weight capacity of the knapsack
    
    Returns:
        List[Tuple[int, int]]: List of selected items (weight, value) that maximize total value
        while staying within weight capacity
    
    Raises:
        ValueError: If max_weight is negative or items contain invalid weights/values
    """
    # Input validation
    if max_weight < 0:
        raise ValueError("Maximum weight must be non-negative")
    
    if any(weight < 0 or value < 0 for weight, value in items):
        raise ValueError("Item weights and values must be non-negative")
    
    # If no items or zero capacity, return empty list
    if not items or max_weight == 0:
        return []
    
    # Dynamic programming solution
    n = len(items)
    # Create DP table: rows are items, columns are weights
    dp = [[0] * (max_weight + 1) for _ in range(n + 1)]
    
    # Build the DP table
    for i in range(1, n + 1):
        weight, value = items[i-1]
        for w in range(max_weight + 1):
            # Don't include current item
            dp[i][w] = dp[i-1][w]
            
            # Try to include current item if possible
            if weight <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w-weight] + value)
    
    # Backtrack to find selected items
    selected_items = []
    w = max_weight
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            # This item was selected
            selected_items.append(items[i-1])
            w -= items[i-1][0]
    
    return selected_items