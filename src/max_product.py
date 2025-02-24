def max_two_number_product(numbers):
    """
    Calculate the maximum product of any two numbers in the given list.

    Args:
        numbers (list): A list of integers.

    Returns:
        int: The maximum product of any two numbers in the list.

    Raises:
        ValueError: If the input list contains fewer than two numbers.
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Validate input
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Check if all elements are integers
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("All list elements must be integers")
    
    # Check list has at least two numbers
    if len(numbers) < 2:
        raise ValueError("List must contain at least two numbers")
    
    # Find the two largest positive numbers or two smallest negative numbers
    # that could produce the maximum product
    largest_nums = sorted(numbers, reverse=True)[:2]
    smallest_nums = sorted(numbers)[:2]
    
    # Return the maximum of the two potential maximum products
    return max(
        largest_nums[0] * largest_nums[1],  # Two largest positive numbers
        smallest_nums[0] * smallest_nums[1]  # Two smallest negative numbers
    )