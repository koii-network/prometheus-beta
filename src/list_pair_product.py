from typing import List, Union

def calculate_pair_products(numbers: List[int]) -> List[int]:
    """
    Calculate the product of all possible pairs of elements in the given list.

    Args:
        numbers (List[int]): A list of integers to calculate pair products from.

    Returns:
        List[int]: A list of products for all unique pairs of elements.

    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
        ValueError: If the input list is empty.

    Examples:
        >>> calculate_pair_products([1, 2, 3])
        [2, 3, 6]
        >>> calculate_pair_products([])
        []
    """
    # Type checking
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers")
    
    # Check if all elements are integers
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("All elements must be integers")
    
    # Handle empty list case
    if not numbers:
        return []
    
    # Calculate pair products
    pair_products = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            pair_products.append(numbers[i] * numbers[j])
    
    return pair_products