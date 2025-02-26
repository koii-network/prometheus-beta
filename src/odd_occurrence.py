def find_odd_occurrence(numbers):
    """
    Find the smallest number that appears an odd number of times in the list using bitwise XOR.
    
    Args:
        numbers (list): A list of integers
    
    Returns:
        int: The smallest number that appears an odd number of times
    
    Raises:
        ValueError: If no number appears an odd number of times or the input list is empty
    """
    # Handle empty list case
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    # First, find all numbers with odd occurrences using bitwise XOR
    odd_occurrence_candidates = set()
    
    # Count occurrences using bitwise XOR trick
    for num in numbers:
        # If the number is already in candidates, remove it
        # If not, add it
        if num in odd_occurrence_candidates:
            odd_occurrence_candidates.remove(num)
        else:
            odd_occurrence_candidates.add(num)
    
    # If no number appears an odd number of times
    if not odd_occurrence_candidates:
        raise ValueError("No number appears an odd number of times")
    
    # Return the smallest number with odd occurrences
    return min(odd_occurrence_candidates)