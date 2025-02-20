def get_unique_pairs(numbers):
    """
    Returns all unique pairs of elements from a given list of integers.
    
    Args:
        numbers (list): A list of integers.
    
    Returns:
        list: A list of tuples representing unique pairs of elements.
              Pairs are sorted in ascending order and are unique.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If any element in the list is not an integer.
    """
    # Validate input
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Check if all elements are integers
    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("All elements must be integers")
    
    # Use set to remove duplicates and prevent repeated pairs
    unique_pairs = set()
    
    # Generate all unique pairs
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            # Create a sorted tuple to ensure uniqueness and prevent duplicates
            pair = tuple(sorted((numbers[i], numbers[j])))
            unique_pairs.add(pair)
    
    # Convert set to sorted list for consistent output
    return sorted(list(unique_pairs))