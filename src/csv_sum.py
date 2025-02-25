def sum_csv_numbers(csv_string: str) -> int:
    """
    Parse a comma-separated string of numbers and return their sum.

    Args:
        csv_string (str): A string of comma-separated integers.

    Returns:
        int: The sum of all numbers in the input string.

    Raises:
        ValueError: If the input string contains non-integer values.
    """
    # Handle empty string case
    if not csv_string:
        return 0

    # Split the string and convert to integers
    try:
        numbers = [int(num.strip()) for num in csv_string.split(',')]
    except ValueError:
        raise ValueError("Input must be a comma-separated string of integers")

    # Return the sum of numbers
    return sum(numbers)