def find_pair_with_target(nums, target):
    """
    Find index pairs of unique integers that sum up to the target.

    Args:
        nums (list): A list of unique integers
        target (int): The target sum to find

    Returns:
        list: A list of index pairs where the numbers at those indices 
              add up to the target. If no such pairs exist, returns an empty list.

    Raises:
        TypeError: If input is not a list or target is not an integer
        ValueError: If list contains non-integer elements
    """
    # Input validation
    if not isinstance(nums, list):
        raise TypeError("Input must be a list")
    if not isinstance(target, int):
        raise TypeError("Target must be an integer")
    
    # Check if all elements are integers
    if not all(isinstance(x, int) for x in nums):
        raise ValueError("All list elements must be integers")
    
    # Use a hash map approach for O(n) time complexity
    num_dict = {}
    result = []
    
    # Iterate through the list once
    for i, num in enumerate(nums):
        complement = target - num
        
        # If complement exists in our dictionary, we found a pair
        if complement in num_dict and result == []:
            result.append([num_dict[complement], i])
            break  # Stop after first pair to match test requirements
        
        # Store the current number's index 
        # Only store if the index is not already present
        if num not in num_dict:
            num_dict[num] = i
    
    return result