def sum_csv_numbers(csv_string):
    """
    Parse a comma-separated string of numbers and return their sum.

    Args:
        csv_string (str): A string of comma-separated integers.

    Returns:
        int: The sum of all numbers in the input string.

    Raises:
        ValueError: If the input is not a valid comma-separated string of integers.
    """
    # Handle empty string case
    if not csv_string:
        return 0

    try:
        # Split the string and convert each element to an integer
        numbers = [int(num.strip()) for num in csv_string.split(',')]
        
        # Return the sum of the numbers
        return sum(numbers)
    except ValueError:
        # Raise an error if any element cannot be converted to an integer
        raise ValueError("Input must be a comma-separated string of integers")