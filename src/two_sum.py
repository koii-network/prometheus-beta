def two_sum(nums, target):
    """
    Find two indices in an array that add up to a target sum.

    Args:
        nums (list): A list of integers to search through
        target (int): The target sum to find

    Returns:
        list: A list containing two indices where the corresponding 
              values add up to the target sum, or an empty list if 
              no such indices exist.

    Time Complexity: O(n)
    Space Complexity: O(n)

    Raises:
        TypeError: If input is not a list or target is not an integer
        ValueError: If either input list or target is empty/None
    """
    # Input validation
    if nums is None or target is None:
        raise ValueError("Input list and target must not be None")
    
    if not isinstance(nums, list):
        raise TypeError("Input must be a list")
    
    if not isinstance(target, int):
        raise TypeError("Target must be an integer")
    
    # Use a dictionary to track complement values
    complement_dict = {}
    
    for index, num in enumerate(nums):
        complement = target - num
        
        # Check if complement exists in dictionary
        if complement in complement_dict:
            return [complement_dict[complement], index]
        
        # Store current number's index
        complement_dict[num] = index
    
    # If no solution found
    return []