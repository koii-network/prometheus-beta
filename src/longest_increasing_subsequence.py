def longest_increasing_subsequence(arr):
    """
    Calculate the length of the longest increasing subsequence in the given array.
    
    Args:
        arr (list): An array of integers
    
    Returns:
        int: Length of the longest increasing subsequence
    
    Time complexity: O(n^2)
    Space complexity: O(n)
    """
    if not arr:
        return 0
    
    # Initialize an array to store LIS lengths
    n = len(arr)
    lis = [1] * n
    
    # Compute LIS values in bottom-up manner
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                lis[i] = max(lis[i], lis[j] + 1)
    
    # Return the maximum value in lis array
    return max(lis)