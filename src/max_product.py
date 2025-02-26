def find_max_product(numbers):
    """
    Find the maximum product of any two numbers in the given list.

    Args:
        numbers (list): A list of integers.

    Returns:
        int: The maximum product of any two numbers in the list.

    Raises:
        ValueError: If the input list contains fewer than two numbers.
        TypeError: If the input is not a list or contains non-numeric elements.
    """
    # Validate input
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Check for non-numeric elements
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("All elements must be numeric")
    
    # Check list length
    if len(numbers) < 2:
        raise ValueError("List must contain at least two numbers")
    
    # Sort the list to handle both positive and negative numbers efficiently
    sorted_nums = sorted(numbers)
    
    # Compare the product of two largest positive numbers 
    # with the product of two smallest negative numbers
    return max(
        sorted_nums[-1] * sorted_nums[-2],  # Two largest positive numbers
        sorted_nums[0] * sorted_nums[1]     # Two smallest (potentially negative) numbers
    )