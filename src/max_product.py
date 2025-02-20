def max_two_number_product(numbers):
    """
    Calculate the maximum product of any two numbers in the given list.
    
    Args:
        numbers (list): A list of integers
    
    Returns:
        int: The maximum product of two numbers in the list
    
    Raises:
        ValueError: If the list contains fewer than two numbers
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two numbers")
    
    # Sort the list in descending order
    sorted_nums = sorted(numbers, reverse=True)
    
    # Consider two scenarios:
    # 1. Product of two largest positive numbers
    # 2. Product of two smallest negative numbers (if they exist)
    return max(
        sorted_nums[0] * sorted_nums[1],  # Two largest numbers
        sorted_nums[-1] * sorted_nums[-2]  # Two smallest numbers
    )