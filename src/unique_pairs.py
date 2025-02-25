from typing import List, Tuple

def find_unique_pairs(numbers: List[int]) -> List[Tuple[int, int]]:
    """
    Find all unique pairs of elements from the given list of integers.
    
    A unique pair is a combination of two distinct elements, where the order doesn't matter.
    For example, (1, 2) and (2, 1) are considered the same pair.
    
    Args:
        numbers (List[int]): Input list of integers
    
    Returns:
        List[Tuple[int, int]]: List of unique pairs of integers
    
    Raises:
        TypeError: If input is not a list
    
    Examples:
        >>> find_unique_pairs([1, 2, 3])
        [(1, 2), (1, 3), (2, 3)]
        >>> find_unique_pairs([])
        []
        >>> find_unique_pairs([1])
        []
    """
    # Validate input
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # If list has less than 2 elements, return empty list
    if len(numbers) < 2:
        return []
    
    # Use set to remove duplicates, then sort to ensure consistent results
    unique_numbers = sorted(set(numbers))
    
    # Generate unique pairs
    unique_pairs = []
    for i in range(len(unique_numbers)):
        for j in range(i+1, len(unique_numbers)):
            unique_pairs.append((unique_numbers[i], unique_numbers[j]))
    
    return unique_pairs