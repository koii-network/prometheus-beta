def calculate_pair_products(numbers):
    """
    Calculate the product of all unique pairs of elements in a given list of integers.

    Args:
        numbers (list): A list of integers.

    Returns:
        list: A list of products for all unique pairs of elements.

    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
        ValueError: If the input list is empty or has fewer than 2 elements.
    """
    # Validate input
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Check if list has fewer than 2 elements
    if len(numbers) < 2:
        raise ValueError("Input list must have at least 2 elements")
    
    # Validate all elements are integers
    if not all(isinstance(x, int) for x in numbers):
        raise TypeError("All elements must be integers")
    
    # Calculate products of all unique pairs
    pair_products = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            pair_products.append(numbers[i] * numbers[j])
    
    return sorted(pair_products)