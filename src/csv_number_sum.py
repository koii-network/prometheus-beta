def sum_csv_numbers(csv_string):
    """
    Parse a comma-separated string of numbers and return their sum.
    
    Args:
        csv_string (str): A string of comma-separated integers
    
    Returns:
        int: Sum of all numbers in the string
    
    Raises:
        ValueError: If the input string contains non-numeric characters (except commas)
    """
    # Check if the string is empty
    if not csv_string:
        return 0
    
    # Split the string by commas
    numbers = csv_string.split(',')
    
    # Convert and sum the numbers
    try:
        return sum(int(num.strip()) for num in numbers)
    except ValueError:
        raise ValueError("Input string must contain only integers and commas")