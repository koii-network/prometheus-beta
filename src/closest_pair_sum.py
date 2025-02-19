def find_closest_pair_sum(arr, target):
    """
    Find the pair of elements in an array whose sum is closest to the target value.
    
    Args:
        arr (list): Input list of numbers
        target (int/float): Target sum value
    
    Returns:
        tuple: A pair of elements from the array whose sum is closest to the target
    
    Raises:
        ValueError: If the input array has fewer than 2 elements
    """
    if len(arr) < 2:
        raise ValueError("Array must have at least 2 elements")
    
    # Initialize variables to track the closest pair
    closest_pair = (arr[0], arr[1])
    min_diff = abs(sum(closest_pair) - target)
    
    # Compare all possible pairs
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            current_pair = (arr[i], arr[j])
            current_diff = abs(sum(current_pair) - target)
            
            # Update if current pair is closer to target
            if current_diff < min_diff:
                min_diff = current_diff
                closest_pair = current_pair
    
    return closest_pair