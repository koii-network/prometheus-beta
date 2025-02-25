def find_closest_pair_sum(arr, target):
    """
    Find the pair of elements in an array whose sum is closest to the target value.
    
    Args:
        arr (list): Input list of numbers
        target (int/float): Target sum to find closest pair to
    
    Returns:
        tuple: A tuple containing the two elements that sum closest to the target
    
    Raises:
        ValueError: If the input array has fewer than 2 elements
    """
    # Check for valid input
    if not arr or len(arr) < 2:
        raise ValueError("Array must contain at least two elements")
    
    # Initialize variables to track the closest pair
    smallest_diff = float('inf')
    closest_pair = None
    
    # Compare every possible pair of elements
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            current_sum = arr[i] + arr[j]
            current_diff = abs(current_sum - target)
            
            # Update closest pair if current pair is closer to target
            # Prioritize pairs closer to the target, and in case of equal difference
            # keep the first occurrence
            if current_diff < smallest_diff or (current_diff == smallest_diff and closest_pair is None):
                smallest_diff = current_diff
                closest_pair = (arr[i], arr[j])
    
    return closest_pair