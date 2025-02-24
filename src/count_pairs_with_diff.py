def count_pairs_with_difference_of_five(numbers):
    """
    Count the number of adjacent pairs in a list with a difference of 5.

    Args:
        numbers (list): A list of integers to check for pairs.

    Returns:
        int: The number of adjacent pairs with a difference of 5.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains non-integer elements.
    """
    # Validate input type
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")

    # Validate list contents
    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("All elements must be integers")

    # Count pairs with difference of 5
    pair_count = 0
    for i in range(len(numbers) - 1):
        # Check absolute difference, regardless of order
        if abs(numbers[i] - numbers[i+1]) == 5:
            pair_count += 1

    return pair_count