from typing import List

def find_most_frequent_index(numbers: List[int]) -> int:
    """
    Find the index of the integer with the highest frequency in the list.
    In case of a tie, return the index of the first occurrence.
    
    Args:
        numbers (List[int]): Input list of integers
    
    Returns:
        int: Index of the most frequent integer
    
    Raises:
        ValueError: If the input list is empty
    """
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    # Count frequencies of each number
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    
    # Find the maximum frequency
    max_freq = max(frequency.values())
    
    # Find the first index of a number with max frequency
    for i, num in enumerate(numbers):
        if frequency[num] == max_freq:
            return i