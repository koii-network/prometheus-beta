from typing import List, Tuple, Optional

def solve_knapsack(items: List[Tuple[int, int]], max_weight: int) -> Tuple[int, List[int]]:
    """
    Solve the 0/1 Knapsack Problem using dynamic programming.
    
    Args:
        items (List[Tuple[int, int]]): A list of (weight, value) tuples representing items.
        max_weight (int): Maximum weight capacity of the knapsack.
    
    Returns:
        Tuple[int, List[int]]: A tuple containing the maximum value and the indices of selected items.
    """
    # Handle edge cases
    if not items or max_weight <= 0:
        return 0, []
    
    # Number of items
    n = len(items)
    
    # Create DP table
    # Rows represent items, columns represent weights from 0 to max_weight
    dp = [[0] * (max_weight + 1) for _ in range(n + 1)]
    
    # Build the DP table
    for i in range(1, n + 1):
        weight, value = items[i-1]
        for w in range(max_weight + 1):
            # If current item can't be included
            if weight > w:
                dp[i][w] = dp[i-1][w]
            else:
                # Max of including or excluding the current item
                dp[i][w] = max(
                    dp[i-1][w],  # Exclude current item
                    dp[i-1][w-weight] + value  # Include current item
                )
    
    # Traceback to find selected items
    selected_items = []
    w = max_weight
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            # Item was included
            selected_items.append(i-1)
            w -= items[i-1][0]
    
    # Return maximum value and indices of selected items (in original order)
    return dp[n][max_weight], list(reversed(selected_items))