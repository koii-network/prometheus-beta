def find_longest_consecutive_sequence(nums):
    """
    Find the longest consecutive sequence of numbers in the input list.

    Args:
        nums (list): A list of integers.
    
    Returns:
        list: The longest consecutive sequence of numbers.
               If multiple sequences of the same length exist, 
               returns the first one encountered.
               Returns an empty list if no sequence is found.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Examples:
        >>> find_longest_consecutive_sequence([100, 4, 200, 1, 3, 2])
        [1, 2, 3, 4]
        >>> find_longest_consecutive_sequence([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
        [0, 1, 2, 3, 4, 5, 6, 7, 8]
    """
    # Handle empty input
    if not nums:
        return []
    
    # Convert list to set for O(1) lookup
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
    
    # If no consecutive sequence found, return a single max/min element
    return longest_sequence if longest_sequence else [max(nums)]