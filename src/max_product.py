def max_two_number_product(numbers):
    """
    Calculate the maximum product of any two numbers in the given list.

    Args:
        numbers (list): A list of integers.

    Returns:
        int: The maximum product of any two numbers in the list.

    Raises:
        ValueError: If the input list contains fewer than two numbers.
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Validate input
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Check if all elements are integers
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("All list elements must be integers")
    
    # Check list has at least two numbers
    if len(numbers) < 2:
        raise ValueError("List must contain at least two numbers")
    
    # Find the maximum product by checking all pairs
    max_prod = float('-inf')
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            max_prod = max(max_prod, numbers[i] * numbers[j])
    
    return max_prod