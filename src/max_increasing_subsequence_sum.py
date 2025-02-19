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
    
    # Will store the end values and their corresponding sums of subsequences
    subsequences = [(arr[0], arr[0])]
    max_sum = arr[0]
    
    for num in arr[1:]:
        # Case 1: Start a new subsequence if num is smaller
        if num <= subsequences[0][0]:
            subsequences[0] = (num, num)
            continue
        
        # Case 2: Extend the longest subsequence
        if num > subsequences[-1][0]:
            prev_sum = subsequences[-1][1]
            subsequences.append((num, prev_sum + num))
            max_sum = max(max_sum, subsequences[-1][1])
            continue
        
        # Case 3: Find the right place to insert/replace
        left, right = 0, len(subsequences) - 1
        while left < right:
            mid = (left + right) // 2
            if subsequences[mid][0] < num:
                left = mid + 1
            else:
                right = mid
        
        # Update the subsequence
        if left > 0:
            new_sum = subsequences[left-1][1] + num
            if new_sum > subsequences[left][1]:
                subsequences[left] = (num, new_sum)
        
        max_sum = max(max_sum, subsequences[left][1])
    
    return max_sum