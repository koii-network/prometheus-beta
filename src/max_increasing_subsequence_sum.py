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
    
    # Track the maximum sums for each ending index
    sums = [arr[0]]
    
    for num in arr[1:]:
        # Find the longest valid subsequence this num can extend
        pos = len(sums)
        for i in range(len(sums)):
            if sums[i] < num or (i > 0 and sums[i-1] >= num):
                pos = i
                break
        
        # Update the sum or add a new subsequence
        if pos == len(sums):
            sums.append(num)
        else:
            # If first element, just replace
            if pos == 0:
                sums[pos] = num
            else:
                # Extend with previous sum
                sums[pos] = sums[pos-1] + num
    
    return max(sums)