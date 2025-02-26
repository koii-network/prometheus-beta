def sum_even_positive_integers(numbers):
    """
    Calculate the sum of all even positive integers in the given list.

    Args:
        numbers (list): A list of integers to process.

    Returns:
        int: The sum of all even positive integers in the list.

    Examples:
        >>> sum_even_positive_integers([1, 2, 3, 4, 5, 6])
        12
        >>> sum_even_positive_integers([-1, -2, 0, 2, 4])
        6
        >>> sum_even_positive_integers([])
        0
    """
    return sum(num for num in numbers if num > 0 and num % 2 == 0)