def sum_positive_even_numbers(numbers):
    """
    Calculate the sum of all positive even numbers in the given list.

    Args:
        numbers (list): A list of integers to process.

    Returns:
        int: The sum of all positive even numbers in the list.
             Returns 0 if no positive even numbers are found.

    Examples:
        >>> sum_positive_even_numbers([1, 2, 3, 4, 5, 6])
        12
        >>> sum_positive_even_numbers([-1, -2, 1, 3, 4, 6])
        10
        >>> sum_positive_even_numbers([1, 3, 5])
        0
    """
    # Filter the list to include only positive even numbers
    positive_even_numbers = [num for num in numbers if num > 0 and num % 2 == 0]
    
    # Return the sum of those numbers
    return sum(positive_even_numbers)