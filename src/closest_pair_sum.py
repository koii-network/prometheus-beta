def find_closest_pair_sum(arr, target):
    """
    Find the pair of elements in an array whose sum is closest to a target value.
    
    Args:
        arr (list): Input list of numbers
        target (int/float): Target sum value
    
    Returns:
        tuple: A tuple containing the two elements that form the closest sum, 
               or None if the input array has fewer than 2 elements
    
    Raises:
        TypeError: If input is not a list or target is not a number
        ValueError: If the list contains non-numeric elements
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not isinstance(target, (int, float)):
        raise TypeError("Target must be a number")
    
    # Check for non-numeric elements
    if not all(isinstance(x, (int, float)) for x in arr):
        raise ValueError("All list elements must be numeric")
    
    # If array has fewer than 2 elements, return None
    if len(arr) < 2:
        return None
    
    # Initialize variables
    closest_sum = float('inf')
    closest_pair = None
    
    # Brute force approach to find the closest pair
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            current_sum = arr[i] + arr[j]
            current_diff = abs(current_sum - target)
            
            # Update if current pair is closer or first occurrence of equal closeness
            if current_diff < abs(closest_sum - target) or closest_pair is None:
                closest_sum = current_sum
                closest_pair = (arr[i], arr[j])
    
    return closest_pair