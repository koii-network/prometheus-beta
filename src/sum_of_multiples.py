def sum_of_multiples(min: int, max: int) -> int:
    """
    Calculate the sum of all multiples of 2 and 3 within an inclusive range.

    Args:
        min (int): The lower bound of the range (inclusive)
        max (int): The upper bound of the range (inclusive)

    Returns:
        int: The sum of all numbers in the range that are multiples of 2 or 3

    Raises:
        ValueError: If min is greater than max
    """
    # Validate input
    if min > max:
        raise ValueError("Minimum value must not be greater than maximum value")

    # Use a set to avoid counting numbers that are multiples of both 2 and 3 twice
    multiples = set()

    # Find multiples of 2 or 3
    for num in range(min, max + 1):
        if num % 2 == 0 or num % 3 == 0:
            multiples.add(num)

    # Return the sum of unique multiples
    return sum(multiples)