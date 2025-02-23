def min_sequence_reconstruction(original, current):
    """
    Determine the minimum number of insertions and removals required to 
    reconstruct the original sequence from the current sequence.
    
    Args:
        original (list): The target original sequence.
        current (list): The current sequence to be transformed.
    
    Returns:
        int: The minimum number of insertions and removals needed.
    
    Raises:
        ValueError: If input is not a list or inputs are None.
    """
    # Validate inputs
    if original is None or current is None:
        raise ValueError("Input sequences cannot be None")
    
    if not isinstance(original, list) or not isinstance(current, list):
        raise ValueError("Inputs must be lists")
    
    # If either list is empty, return the length of the other list
    if not original:
        return len(current)
    if not current:
        return len(original)
    
    # Convert lists to sets for efficient comparisons
    original_set = set(original)
    current_set = set(current)
    
    # Elements to be removed (in current but not in original)
    removals = len(current_set - original_set)
    
    # Elements to be inserted (in original but not in current)
    insertions = len(original_set - current_set)
    
    return removals + insertions