def calculate_pair_products(numbers):
    """
    Calculate the product of all pairs of elements in a given list of integers.
    
    Args:
        numbers (list): A list of integers
    
    Returns:
        list: A list of products for all unique pairs of numbers in the input list
    
    Raises:
        TypeError: If the input is not a list
        ValueError: If the input list contains non-integer elements
    """
    # Validate input type
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Validate list contains only integers
    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("All elements must be integers")
    
    # Calculate products of all unique pairs
    pair_products = [
        numbers[i] * numbers[j] 
        for i in range(len(numbers)) 
        for j in range(i+1, len(numbers))
    ]
    
    return pair_products