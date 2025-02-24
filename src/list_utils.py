from typing import List


def find_duplicates(numbers: List[int]) -> List[int]:
    """
    Find and return a list of duplicate integers from the input list.

    Args:
        numbers (List[int]): A list of integers to search for duplicates.

    Returns:
        List[int]: A list of integers that appear more than once in the input list.
                   Duplicates are returned only once, in the order of their first appearance.

    Examples:
        >>> find_duplicates([1, 2, 3, 4, 2, 5, 6, 3, 7])
        [2, 3]
        >>> find_duplicates([1, 1, 1, 1])
        [1]
        >>> find_duplicates([])
        []
    """
    # Use a dictionary to track first appearance and duplicate status
    duplicate_tracker = {}
    
    # First pass: track occurrences
    for num in numbers:
        if num in duplicate_tracker:
            duplicate_tracker[num] += 1
        else:
            duplicate_tracker[num] = 1
    
    # Second pass: collect duplicates in order of first appearance
    duplicates = []
    seen_duplicates = set()
    for num in numbers:
        if duplicate_tracker[num] > 1 and num not in seen_duplicates:
            duplicates.append(num)
            seen_duplicates.add(num)
    
    return duplicates