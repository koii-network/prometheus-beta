def find_longest_increasing_subsequence(arr):
    """
    Find the longest increasing subsequence in a given array of integers.
    
    Args:
        arr (list): A list of integers to find the longest increasing subsequence in.
    
    Returns:
        tuple: A tuple containing two elements:
            - int: Length of the longest increasing subsequence
            - list: The longest increasing subsequence itself
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-integer elements
    
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    
    Examples:
        >>> find_longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80])
        (6, [10, 22, 33, 50, 60, 80])
        >>> find_longest_increasing_subsequence([])
        (0, [])
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list
    if not arr:
        return 0, []
    
    # Validate all elements are integers
    if not all(isinstance(x, int) for x in arr):
        raise ValueError("All elements must be integers")
    
    # Length of the input array
    n = len(arr)
    
    # Dynamic programming approach
    # lengths will store the length of LIS ending at each index
    lengths = [1] * n
    
    # prev will help us reconstruct the subsequence
    prev = [-1] * n
    
    # Find the longest increasing subsequence
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and lengths[i] < lengths[j] + 1:
                lengths[i] = lengths[j] + 1
                prev[i] = j
    
    # Find the index of maximum length
    max_length_index = lengths.index(max(lengths))
    
    # Reconstruct the subsequence
    subsequence = []
    current = max_length_index
    while current != -1:
        subsequence.insert(0, arr[current])
        current = prev[current]
    
    return len(subsequence), subsequence