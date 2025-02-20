def reorder_consecutive_integers(nums):
    """
    Reorder a list of integers so that the difference between consecutive 
    elements is always 1, -1, or 0. If impossible, return None.
    
    Args:
        nums (list): A list of integers to be reordered
    
    Returns:
        list or None: Reordered list or None if reordering is impossible
    """
    if not nums:
        return []
    
    # Sort the input list to help with reordering
    nums = sorted(nums)
    n = len(nums)
    
    # Try different starting points
    for start_idx in range(n):
        result = [nums[start_idx]]
        used = {start_idx}
        
        # Build the reordered list
        while len(result) < n:
            # Find the next valid number
            found_next = False
            for j in range(n):
                if j in used:
                    continue
                
                # Check if the difference is 0, 1, or -1
                diff = abs(result[-1] - nums[j])
                if diff <= 1:
                    result.append(nums[j])
                    used.add(j)
                    found_next = True
                    break
            
            # If no valid next number found, break the attempt
            if not found_next:
                break
        
        # Check if we successfully reordered the entire list
        if len(result) == n:
            return result
    
    return None