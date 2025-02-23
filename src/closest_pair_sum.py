def find_closest_pair_sum(arr, target):
    """
    Find the pair of elements in the array whose sum is closest to the target value.
    
    Args:
        arr (list): Input list of numbers
        target (int/float): Target sum to find closest match
    
    Returns:
        tuple: A tuple containing two elements that sum closest to the target.
               If multiple pairs have equal closeness, returns the first occurrence.
    
    Raises:
        ValueError: If the input array has fewer than 2 elements
    """
    # Validate input
    if not arr or len(arr) < 2:
        raise ValueError("Array must contain at least two elements")
    
    # Initialize variables to track the closest pair
    closest_sum = float('inf')
    closest_pair = None
    
    # Check all possible pairs
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            current_sum = arr[i] + arr[j]
            
            # Update closest pair if current pair is closer to target
            current_diff = abs(current_sum - target)
            closest_diff = abs(closest_sum - target)
            
            if current_diff < closest_diff or \
               (current_diff == closest_diff and closest_pair is None):
                closest_sum = current_sum
                closest_pair = (arr[i], arr[j])
    
    return closest_pair