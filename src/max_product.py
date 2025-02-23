def max_product_of_two_numbers(numbers):
    """
    Find the maximum product of any two numbers in the given list.
    
    Args:
        numbers (list): A list of integers
    
    Returns:
        int: The maximum product of any two numbers in the list
    
    Raises:
        ValueError: If the list contains fewer than 2 numbers
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two numbers")
    
    # Sort the list in descending order
    sorted_nums = sorted(numbers, reverse=True)
    
    # Consider two scenarios:
    # 1. Product of two largest positive numbers
    # 2. Product of two smallest numbers (in case of large negative numbers)
    return max(
        sorted_nums[0] * sorted_nums[1],  # Two largest numbers
        sorted_nums[-1] * sorted_nums[-2]  # Two smallest numbers
    )