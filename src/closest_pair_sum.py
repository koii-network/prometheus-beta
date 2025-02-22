def find_closest_pair_sum(arr, target):
    """
    Find the pair of elements in the array whose sum is closest to the target value.
    
    Args:
        arr (list): Input list of numbers
        target (int): Target sum to find
    
    Returns:
        tuple: A pair of numbers from the array that have the closest sum to the target
               If multiple pairs have equal closeness, returns the first occurrence
    
    Raises:
        ValueError: If the input array has fewer than 2 elements
    """
    if len(arr) < 2:
        raise ValueError("Array must contain at least two elements")
    
    # Initialize variables to track the closest pair and minimum difference
    closest_pair = (arr[0], arr[1])
    min_diff = abs(arr[0] + arr[1] - target)
    
    # Compare all possible pairs
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            current_sum = arr[i] + arr[j]
            current_diff = abs(current_sum - target)
            
            # Update closest pair if:
            # 1. Current difference is smaller, or
            # 2. Current difference is equal but we want the first occurrence
            if current_diff < min_diff:
                min_diff = current_diff
                closest_pair = (arr[i], arr[j])
    
    return closest_pair