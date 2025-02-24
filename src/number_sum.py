def sum_comma_separated_numbers(number_string: str) -> int:
    """
    Parse a comma-separated string of numbers and return their sum.

    Args:
        number_string (str): A string of comma-separated integers.

    Returns:
        int: The sum of all numbers in the input string.

    Raises:
        ValueError: If the input string contains non-numeric characters (except commas).
    """
    # Handle empty string case
    if not number_string:
        return 0

    # Split the string by commas and convert to integers
    try:
        numbers = [int(num.strip()) for num in number_string.split(',')]
    except ValueError:
        raise ValueError("Input string must contain only integers and commas")

    # Return the sum of the numbers
    return sum(numbers)