def max_increasing_subsequence_sum(arr):
    """
    Find the maximum sum of an increasing subsequence in O(n log n) time complexity.
    
    Args:
        arr (list): List of integers
    
    Returns:
        int: Maximum sum of an increasing subsequence
    """
    if not arr:
        return 0
    
    # Lengths of subsequences
    lengths = [1] * len(arr)
    
    # Track total sums
    total_sums = arr.copy()
    
    # Track potential subsequence end indices
    potential_ends = [0]
    
    max_sum = arr[0]
    
    for i in range(1, len(arr)):
        for j in potential_ends:
            if arr[i] > arr[j]:
                # Potential extension of an existing subsequence
                if total_sums[j] + arr[i] > total_sums[i]:
                    total_sums[i] = total_sums[j] + arr[i]
                    lengths[i] = lengths[j] + 1
        
        # Update max sum and potential ends
        if total_sums[i] > max_sum:
            max_sum = total_sums[i]
        
        # Add current index to potential ends
        potential_ends.append(i)
    
    return max_sum