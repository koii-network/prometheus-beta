def reorder_consecutive_diff(nums):
    """
    Reorder a list of integers so that the difference between 
    consecutive elements is always 1, -1, or 0.
    
    Args:
        nums (list): List of integers to reorder
    
    Returns:
        list or None: Reordered list or None if impossible
    """
    if not nums:
        return []
    
    # Create a set of available numbers for easy lookup
    available = set(nums)
    result = [nums[0]]
    available.remove(nums[0])
    
    # Try to build the list around the first element
    while available:
        # Look for a number that can be added to the end
        found = False
        for num in available:
            # Check if the difference is acceptable (1, -1, or 0)
            diff = abs(num - result[-1])
            if diff <= 1:
                result.append(num)
                available.remove(num)
                found = True
                break
        
        # If no acceptable number found, look for a number at the start
        if not found:
            for num in available:
                diff = abs(num - result[0])
                if diff <= 1:
                    result.insert(0, num)
                    available.remove(num)
                    found = True
                    break
        
        # If still no number found, it's impossible to reorder
        if not found:
            return None
    
    return result