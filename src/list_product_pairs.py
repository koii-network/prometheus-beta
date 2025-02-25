from typing import List, Optional

def calculate_product_pairs(numbers: List[int]) -> Optional[List[int]]:
    """
    Calculate the product of all pairs of elements in a given list of integers.

    Args:
        numbers (List[int]): A list of integers to calculate pair products from.

    Returns:
        Optional[List[int]]: A list of products for all unique pairs of elements,
        or None if the input list is None or empty.

    Raises:
        TypeError: If the input is None or contains non-integer elements.

    Examples:
        >>> calculate_product_pairs([1, 2, 3])
        [2, 3, 6]
        >>> calculate_product_pairs([])
        None
        >>> calculate_product_pairs([5])
        None
    """
    # Explicitly handle None input
    if numbers is None:
        raise TypeError("Input cannot be None")
    
    # Handle empty list input
    if not numbers:
        return None
    
    # Validate input is a list of integers
    if not all(isinstance(x, int) for x in numbers):
        raise TypeError("All elements must be integers")
    
    # If list has only one element, return None
    if len(numbers) < 2:
        return None
    
    # Calculate products of all unique pairs
    products = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            products.append(numbers[i] * numbers[j])
    
    return products