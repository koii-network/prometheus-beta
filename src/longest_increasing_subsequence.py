def longest_increasing_subsequence(arr):
    """
    Compute the length of the longest increasing subsequence in an array of integers.
    
    Args:
        arr (list): A list of integers
    
    Returns:
        int: Length of the longest increasing subsequence
    
    Time complexity: O(n^2)
    Space complexity: O(n)
    """
    # Handle empty or None input
    if not arr:
        return 0
    
    # Initialize an array to store lengths of LIS ending at each index
    n = len(arr)
    lis_lengths = [1] * n
    
    # Compute LIS for each element
    for i in range(1, n):
        for j in range(i):
            # If current element is greater than previous elements, 
            # we can potentially extend their subsequence
            if arr[i] > arr[j]:
                lis_lengths[i] = max(lis_lengths[i], lis_lengths[j] + 1)
    
    # Return the maximum length found
    return max(lis_lengths)