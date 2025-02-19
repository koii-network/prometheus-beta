def find_two_sum_indices(numbers, target_sum):
    """
    Find two indices in an array that add up to a target sum.
    
    Args:
        numbers (list): A list of integers
        target_sum (int): The target sum to find
    
    Returns:
        list: A list of two indices where the corresponding numbers add up to the target sum,
              or an empty list if no such indices are found
    
    Raises:
        TypeError: If input is not a list or target_sum is not an integer
        ValueError: If list contains non-numeric elements
    """
    # Input validation
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    if not isinstance(target_sum, int):
        raise TypeError("Target sum must be an integer")
    
    # Check if all elements are numeric
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("List must contain only numeric elements")
    
    # Create a hash map to store complement values and their indices
    complement_map = {}
    
    for i, num in enumerate(numbers):
        complement = target_sum - num
        
        # If complement exists in the map, we found our pair
        if complement in complement_map:
            return [complement_map[complement], i]
        
        # Store the current number's index
        complement_map[num] = i
    
    # If no solution is found, return an empty list
    return []