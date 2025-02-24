def calculate_pair_products(numbers):
    """
    Calculate the product of all unique pairs of elements in a given list of integers.

    Args:
        numbers (list): A list of integers.

    Returns:
        list: A list of products for all unique pairs of elements.

    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
        ValueError: If the input list is empty.
    """
    # Validate input
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Check if list is empty
    if len(numbers) == 0:
        raise ValueError("Input list cannot be empty")
    
    # Validate all elements are integers
    if not all(isinstance(x, int) for x in numbers):
        raise TypeError("All elements must be integers")
    
    # Calculate products of all unique pairs
    pair_products = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            pair_products.append(numbers[i] * numbers[j])
    
    return pair_products