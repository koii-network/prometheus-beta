def find_longest_consecutive_sequence(nums):
    """
    Find the longest consecutive sequence in a list of integers.
    
    Args:
        nums (list): A list of integers
    
    Returns:
        list: The longest consecutive sequence of integers
    """
    # Handle empty list case
    if not nums:
        return []
    
    # Convert to set for O(1) lookup
    num_set = set(nums)
    
    longest_sequence = []
    
    for num in num_set:
        # Check if this is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_sequence = [current_num]
            
            # Extend the sequence as long as consecutive numbers exist
            while current_num + 1 in num_set:
                current_num += 1
                current_sequence.append(current_num)
            
            # Update longest sequence if current is longer
            if len(current_sequence) > len(longest_sequence):
                longest_sequence = current_sequence
    
    return longest_sequence