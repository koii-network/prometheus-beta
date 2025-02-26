from typing import List, Set
from itertools import combinations

def count_equal_sum_partitions(numbers: List[int]) -> int:
    """
    Calculate the number of ways a group of distinct numbers can be partitioned 
    into two subsets with equal sums.

    Args:
        numbers (List[int]): A list of distinct integers to partition.

    Returns:
        int: The number of unique ways to partition the numbers into two 
             subsets with equal total sums.

    Raises:
        ValueError: If the input list is empty or contains duplicates.
    """
    # Validate input
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    if len(set(numbers)) != len(numbers):
        raise ValueError("Input list must contain distinct numbers")

    total_sum = sum(numbers)
    
    # If total sum is odd, no equal partition is possible
    if total_sum % 2 != 0:
        return 0

    target_sum = total_sum // 2
    count = 0

    # Try all possible subset combinations
    for r in range(1, len(numbers) // 2 + 1):
        for subset in combinations(numbers, r):
            # Check if the current subset sums to half the total
            if sum(subset) == target_sum:
                # Complementary subset (more thorough verification)
                complement = tuple(num for num in numbers if num not in subset)
                
                # Ensure we only count unique partitions
                if sum(complement) == target_sum and hash(subset) < hash(complement):
                    count += 1

    return count