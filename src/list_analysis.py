def analyze_list_numbers(numbers):
    """
    Analyze a list of numbers to calculate the sum of even numbers and count of odd numbers.

    Args:
        numbers (list): A list of numbers to analyze.

    Returns:
        tuple: A tuple containing two elements:
            - The sum of all even numbers in the list
            - The count of odd numbers in the list

    Raises:
        TypeError: If the input is not a list or contains non-numeric elements.
    """
    # Validate input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")

    # Validate all elements are numeric
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("All list elements must be numeric")

    # Calculate sum of even numbers and count of odd numbers
    even_sum = sum(num for num in numbers if num % 2 == 0)
    odd_count = sum(1 for num in numbers if num % 2 != 0)

    return even_sum, odd_count