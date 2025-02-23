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
    
    # Count element frequencies
    from collections import Counter
    original_freq = Counter(original)
    current_freq = Counter(current)
    
    # Track total changes
    total_changes = 0
    
    # Check for each unique element
    for elem in set(list(original_freq.keys()) + list(current_freq.keys())):
        orig_count = original_freq[elem]
        curr_count = current_freq[elem]
        total_changes += abs(orig_count - curr_count)
    
    # Always require at least total_changes / 2 (rounding up)
    return (total_changes + 1) // 2