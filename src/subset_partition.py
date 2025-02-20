from typing import List
from itertools import combinations

def count_equal_sum_partitions(numbers: List[int]) -> int:
    """
    Calculate the number of ways a group of numbers can be 
    partitioned into two subsets with equal sums.
    
    Args:
        numbers (List[int]): A list of integers
    
    Returns:
        int: Number of ways to partition the numbers into two equal sum subsets
    
    Raises:
        ValueError: If the input list is empty
    """
    # Validate input
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    # Total sum of the numbers
    total_sum = sum(numbers)
    
    # If total sum is odd, no equal partition is possible
    if total_sum % 2 != 0:
        return 0
    
    # Target sum for each subset
    target_sum = total_sum // 2
    
    # Number of partitions
    partitions = 0
    
    # Dynamic programming solution for subset sum
    n = len(numbers)
    dp = [set() for _ in range(target_sum + 1)]
    dp[0].add(tuple())
    
    for num in numbers:
        for j in range(target_sum, num - 1, -1):
            for subset in list(dp[j - num]):
                new_subset = tuple(sorted(subset + (num,)))
                dp[j].add(new_subset)
    
    # Count unique partitions
    unique_partitions = set()
    for subset in dp[target_sum]:
        complement = tuple(sorted(x for x in numbers if x not in subset))
        if sum(subset) == sum(complement) == target_sum:
            # Use frozenset to avoid order-based duplicates
            partition = frozenset([tuple(sorted(subset)), tuple(sorted(complement))])
            unique_partitions.add(partition)
    
    return len(unique_partitions)