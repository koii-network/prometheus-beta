def sum_integer_list(numbers):
    """
    Calculate the sum of a list of integers using a single loop.

    Args:
        numbers (list): A list of integers to be summed.

    Returns:
        int: The sum of all integers in the list.

    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Validate input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")

    # Validate all elements are integers
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("All elements must be integers")

    # Single loop to calculate sum
    total = 0
    for num in numbers:
        total += num

    return total