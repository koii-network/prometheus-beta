def parse_csv_sum(csv_string: str) -> int:
    """
    Parse a comma-separated string of numbers and return their sum.
    
    Args:
        csv_string (str): A string of comma-separated integers
    
    Returns:
        int: The sum of all numbers in the CSV string
    
    Raises:
        ValueError: If the input string contains non-integer values
    """
    # Handle empty string case
    if not csv_string:
        return 0
    
    # Split the string and convert to integers
    try:
        numbers = [int(num.strip()) for num in csv_string.split(',')]
        return sum(numbers)
    except ValueError:
        raise ValueError("Input string must contain only integers separated by commas")