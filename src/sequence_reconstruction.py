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
    
    # Count element frequencies in both lists
    from collections import Counter
    original_freq = Counter(original)
    current_freq = Counter(current)
    
    # Calculate the total changes needed
    total_changes = 0
    for elem in set(list(original_freq.keys()) + list(current_freq.keys())):
        # For each element, add the absolute min of removals or insertions
        original_count = original_freq[elem]
        current_count = current_freq[elem]
        total_changes += abs(original_count - current_count)
    
    return total_changes // 2  # Divide by 2 as each change is counted twice